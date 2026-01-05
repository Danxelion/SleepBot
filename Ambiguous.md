# SleepBot - Ambiguity Analysis

This document analyzes the **ambiguity** in the SleepBot program from a **Principles of Programming Languages** perspective, identifying resolved and unresolved ambiguous patterns.

---

## 1. Types of Ambiguity in Programming Languages

In formal language theory, **ambiguity** occurs when:
- A grammar produces **multiple parse trees** for the same input string
- A lexer can tokenize input in **multiple ways**
- **Semantic meaning** is unclear from syntax alone

---

## 2. Resolved Ambiguities (Solutions Applied)

### 2.1 Lexical Ambiguity - Keyword vs. Identifier Conflict

**Problem:** The word `"time"` could be interpreted as:
- The `TIMEWORD` token (keyword)
- Part of a `TIME` token (like `"7am"`)

**Solution Applied:**
```antlr
// In SleepCommands.g4
TIMEWORD    : 'time';

TIME
    : DIGIT DIGIT? ':' DIGIT DIGIT (AM_PM)?
    | DIGIT DIGIT? AM_PM
    ;
```

The lexer uses **longest match rule** and **rule order priority** - `TIME` has a specific pattern with digits, so `"time"` (letters only) is matched as `TIMEWORD`.

---

### 2.2 Grammar Ambiguity - Optional Elements

**Problem:** The `sleepCmd` rule has optional elements:
```antlr
sleepCmd
    : (I)? (AM)? GOING TO SLEEP
    ;
```

Multiple inputs could match:
- `"going to sleep"`
- `"i going to sleep"`
- `"i am going to sleep"`
- `"am going to sleep"`

**Solution Applied:**
ANTLR uses **deterministic parsing** with optional `()?` groups. The parser accepts all valid variants without ambiguity because the optionality is clearly defined. Each variant produces a unique parse tree.

---

### 2.3 Synonym Ambiguity - Natural Language Variations

**Problem:** Users express the same intent differently:
- `"heading to bed"` vs. `"going to sleep"` vs. `"about to sleep"`
- `"wake me at"` vs. `"set alarm for"` vs. `"get me up at"`

**Solution Applied:** Text normalization in [chatbot.py](chatbot.py#L19-L55):
```python
def normalize_text(self, text: str) -> str:
    synonyms = {
        "heading to bed": "going to sleep",
        "going to bed": "going to sleep",
        "about to sleep": "going to sleep",
        "wake me at": "wake me up at",
        "get me up at": "wake me up at",
        "set alarm for": "wake me up at",
        # ... more synonyms
    }
```
This **pre-processing step** maps variations to canonical forms before parsing.

---

### 2.4 Time Format Ambiguity

**Problem:** Time can be expressed in multiple formats:
- `"7am"`, `"7AM"`, `"7:00am"`
- `"10:30pm"`, `"10:30PM"`, `"22:30"`

**Solution Applied:** In [alarm_manager.py](alarm_manager.py#L6-L27):
```python
def normalize_time_string(t: str) -> str:
    t = t.strip().lower()  # Case-insensitive
    is_pm = t.endswith("pm")
    is_am = t.endswith("am")
    # ... normalize to HH:MM format
```
All time formats are **normalized to `HH:MM`** format for internal processing.

---

### 2.5 Grammar Alternative Ambiguity

**Problem:** Multiple ways to express the same command:
```antlr
consistencyCmd
    : (SHOW | CHECK) MY SLEEP (CONSISTENCY | REGULARITY)
    | HOW (CONSISTENT | REGULAR) IS MY SLEEP
    ;
```

**Solution Applied:** 
- Using **alternation `|`** at the token level, not rule level
- Each alternative produces the **same semantic action** in the handler
- The parser deterministically chooses based on the first token

---

### 2.6 Dangling Else-like Ambiguity in Command Structure

**Problem:** The main `command` rule has 12 alternatives:
```antlr
command
    : sleepCmd
    | wakeCmd
    | setAlarmCmd
    | setAlarmRelativeCmd
    | cancelAlarmCmd
    | snoozeAlarmCmd
    | lateAlertCmd
    | queryCmd
    | consistencyCmd
    | qualityCmd
    | adviceCmd
    | helpCmd
    ;
```

**Solution Applied:**
- Each command starts with **distinct keyword sequences**
- ANTLR resolves using **lookahead** (LL(*) parsing)
- No two commands share the same prefix that leads to different parses

---

### 2.7 Cancel/Stop Ambiguity

**Problem:** Two words mean the same action:
```antlr
cancelAlarmCmd
    : (CANCEL | STOP) (MY)? ALARM
    ;
```

**Solution Applied:** 
- Both `"cancel alarm"` and `"stop alarm"` are valid
- The semantic action treats them identically
- The alternation `(CANCEL | STOP)` makes this explicit

---

## 3. Unresolved Ambiguities (Potential Issues)

### 3.1 ⚠️ "Sleep" Keyword Overloading

**Problem:** The word `"sleep"` appears in multiple contexts:
- `sleepCmd`: `"going to sleep"` (log sleep action)
- `consistencyCmd`: `"check my sleep consistency"` (query)
- `qualityCmd`: `"check my sleep quality"` (query)
- `adviceCmd`: `"give me sleep advice"` (query)

**Current State:** Partially resolved by distinct prefix keywords, but:
- `"my sleep"` vs `"to sleep"` creates potential confusion
- `"sleep"` is both a verb and noun contextually

**Risk:** If user says `"sleep"` alone, parser may fail.

**Suggested Solution:**
```antlr
// Add fallback pattern
sleepCmd
    : (I)? (AM)? GOING TO SLEEP
    | SLEEP NOW           // New: explicit "sleep now" command
    ;
```

---

### 3.2 ⚠️ Time Token Ambiguity with Numbers

**Problem:** The lexer has overlapping patterns:
```antlr
TIME
    : DIGIT DIGIT? ':' DIGIT DIGIT (AM_PM)?
    | DIGIT DIGIT? AM_PM
    ;

NUMBER
    : DIGIT+
    ;
```

Input like `"7"` alone:
- Could be `NUMBER` (for relative alarm: `"wake me up in 7 minutes"`)
- Could be incomplete `TIME` (for absolute alarm)

**Current State:** ANTLR's longest-match resolves this, but:
- `"7"` → `NUMBER`
- `"7am"` → `TIME`

**Unresolved Case:** `"wake me up at 7"` - Parser expects `TIME`, gets `NUMBER`, fails silently.

**Suggested Solution:**
```python
# In chatbot.py, add context-aware fallback
def handle(self, text: str) -> str:
    # If parser fails with a number, check if it's a time context
    if "at" in normalized and re.search(r'\d{1,2}$', normalized):
        # Assume AM for morning times (6-11), PM for afternoon (12-8)
        ...
```

---

### 3.3 ⚠️ Contextual Ambiguity - "i am" vs "I AM AWAKE"

**Problem:**
```antlr
I   : 'i';
AM  : 'am';
```

Input `"i am"` is tokenized as `I AM`, but:
- `"i am going to sleep"` → Valid `sleepCmd`
- `"i am awake"` → Valid `wakeCmd`
- `"i am tired"` → Parse failure (no handler)

**Current State:** The parser requires complete phrases, but natural language is often incomplete.

**Unresolved:** Partial phrases like `"i am"` alone cause failures with no helpful feedback.

**Suggested Solution:**
```python
# Add pattern for incomplete input
if normalized in ["i am", "i"]:
    return "What would you like to do? Are you going to sleep or waking up?"
```

---

### 3.4 ⚠️ Semantic Ambiguity - "Yesterday" Query

**Problem:** The query command:
```antlr
queryCmd
    : WHAT TIMEWORD DID I SLEEP YESTERDAY
    ;
```

**Semantic Issues:**
1. `"yesterday"` is interpreted as "last sleep session", not literally yesterday
2. If user logged sleep today at 2am, is that "yesterday" or "today"?

**Current Implementation:** [sleep_tracker.py](sleep_tracker.py#L49-L52):
```python
def get_yesterday_sleep_time(self):
    if not self.data:
        return None
    return self.data[-1]["sleep"]  # Returns LAST entry, not yesterday
```

**Unresolved:** The function name and grammar say "yesterday" but returns the most recent entry regardless of date.

**Suggested Solution:**
```python
def get_yesterday_sleep_time(self):
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    
    for entry in reversed(self.data):
        sleep_time = self._parse_time(entry["sleep"])
        if sleep_time.date() == yesterday:
            return entry["sleep"]
    return None
```

---

### 3.5 ⚠️ Snooze Without Active Alarm

**Problem:** The snooze command:
```antlr
snoozeAlarmCmd
    : SNOOZE (FOR)? NUMBER TIMEUNIT
    ;
```

**Unresolved:** User can snooze even if no alarm is active:
```python
# In chatbot.py - snooze always sets new timer
if isinstance(child, SleepCommandsParser.SnoozeAlarmCmdContext):
    minutes = amount * 60 if "hour" in unit else amount
    self.alarm.set_relative_alarm(minutes)  # No check for existing alarm!
```

**Suggested Solution:**
```python
if isinstance(child, SleepCommandsParser.SnoozeAlarmCmdContext):
    if self.alarm.absolute_alarm is None and self.alarm.relative_timer is None:
        return "⚠️ No active alarm to snooze."
    # ... existing logic
```

---

### 3.6 ⚠️ Lexical Ambiguity - Case Sensitivity

**Problem:** Grammar is case-sensitive by default:
```antlr
WAKE : 'wake';
```

But input normalization converts to lowercase:
```python
text = text.lower().strip()
```

**Current State:** Resolved by pre-normalization, but:
- If someone bypasses `normalize_text()`, parsing fails
- API could receive mixed-case input directly

**Suggested Solution:** Use case-insensitive lexer:
```antlr
WAKE : [Ww][Aa][Kk][Ee];
// or
WAKE : 'wake' | 'Wake' | 'WAKE';
```

---

### 3.7 ⚠️ Numeric Unit Ambiguity

**Problem:**
```antlr
TIMEUNIT
    : 'minute' | 'minutes' | 'hour' | 'hours'
    ;
```

**Unresolved:** No validation for singular/plural agreement:
- `"1 minutes"` ✓ (grammatically incorrect but accepted)
- `"30 minute"` ✓ (grammatically incorrect but accepted)

**Impact:** Low priority, but reduces input validation quality.

**Suggested Solution:**
```python
# In chatbot.py, add grammar correction in response
if amount == 1 and "s" in unit:
    display_unit = unit.rstrip("s")  # "minutes" → "minute"
```

---

## 4. Ambiguity Resolution Techniques Used

| Technique | Applied In | Purpose |
|-----------|------------|---------|
| **Longest Match Rule** | Lexer (`TIME` vs `NUMBER`) | Prefer longer token matches |
| **Rule Order Priority** | Lexer (keywords before `TIME`) | Earlier rules take precedence |
| **Deterministic Alternatives** | Parser (`\|` operator) | Clear choice points |
| **Pre-processing Normalization** | `normalize_text()` | Canonicalize synonyms |
| **Post-processing Normalization** | `normalize_time_string()` | Standardize time formats |
| **Context Memory** | `last_intent`, `last_alarm_time` | Disambiguate follow-ups |
| **Exception Handling** | `try/except` around parser | Graceful failure on unparseable input |

---

## 5. Summary Table

| Ambiguity Type | Status | Location | Solution |
|----------------|--------|----------|----------|
| Keyword vs. Time token | ✅ Resolved | Lexer | Pattern specificity |
| Optional grammar elements | ✅ Resolved | Parser | ANTLR `()?` handling |
| Natural language synonyms | ✅ Resolved | `normalize_text()` | Dictionary mapping |
| Time format variations | ✅ Resolved | `normalize_time_string()` | Normalization |
| Cancel/Stop synonyms | ✅ Resolved | Grammar | Alternation `\|` |
| `"sleep"` keyword overloading | ⚠️ Partial | Grammar | Distinct prefixes |
| Time vs. Number overlap | ⚠️ Unresolved | Lexer | Needs context handling |
| Incomplete phrases | ⚠️ Unresolved | Parser | Needs fallback patterns |
| "Yesterday" semantics | ⚠️ Unresolved | `get_yesterday_sleep_time()` | Needs date logic |
| Snooze without alarm | ⚠️ Unresolved | Handler | Needs state check |
| Case sensitivity | ⚠️ Partial | Lexer | Relies on normalization |
| Singular/plural units | ⚠️ Unresolved | Grammar | Low priority |

---

## 6. Recommendations

1. **Add explicit error messages** for common parse failures
2. **Implement date-aware queries** for "yesterday" semantics
3. **Add state validation** for snooze commands
4. **Consider case-insensitive lexer** rules for robustness
5. **Add more fallback synonyms** in pre-processing
6. **Implement fuzzy matching** for near-miss commands

---

## 7. References

- ANTLR Documentation: Lexer Rule Ordering
- Dragon Book: Ambiguous Grammars (Chapter 4.3)
- Principles of Programming Languages: Syntax Analysis
