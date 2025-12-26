grammar SleepCommands;

// =====================================================
// Parser Rules
// =====================================================

command
    : sleepCmd
    | wakeCmd
    | setAlarmCmd
    | setAlarmRelativeCmd
    | cancelAlarmCmd        // ✅ added
    | snoozeAlarmCmd        // ✅ added
    | lateAlertCmd
    | queryCmd
    | consistencyCmd
    | qualityCmd            // ✅ sleep quality
    | adviceCmd             // ✅ sleep advice
    | helpCmd
    ;

// ----------------------------
// Sleep / Wake
// ----------------------------

sleepCmd
    : (I)? (AM)? GOING TO SLEEP
    ;

wakeCmd
    : (I)? (WOKE UP | AM AWAKE)
    ;

// ----------------------------
// Alarm
// ----------------------------

setAlarmCmd
    : WAKE ME UP AT TIME
    ;

setAlarmRelativeCmd
    : WAKE ME UP IN NUMBER TIMEUNIT
    ;

// ----------------------------
// Alarm control
// ----------------------------

cancelAlarmCmd
    : (CANCEL | STOP) (MY)? ALARM
    ;

snoozeAlarmCmd
    : SNOOZE (FOR)? NUMBER TIMEUNIT
    ;

// ----------------------------
// Late alert
// ----------------------------

lateAlertCmd
    : WARN ME IF I AM AWAKE AFTER TIME
    ;

// ----------------------------
// Queries
// ----------------------------

queryCmd
    : WHAT TIMEWORD DID I SLEEP YESTERDAY
    ;

// ----------------------------
// Consistency
// ----------------------------

consistencyCmd
    : (SHOW | CHECK) MY SLEEP (CONSISTENCY | REGULARITY)
    | HOW (CONSISTENT | REGULAR) IS MY SLEEP
    ;

// ----------------------------
// Quality
// ----------------------------

qualityCmd
    : (SHOW | CHECK) MY SLEEP QUALITY
    | HOW IS MY SLEEP QUALITY
    | (RATE | ANALYZE) MY SLEEP
    ;

// ----------------------------
// Advice
// ----------------------------

adviceCmd
    : GIVE ME (SLEEP)? (ADVICE | TIPS | SUGGESTIONS)
    | (SHOW | GET) (SLEEP)? (ADVICE | TIPS | SUGGESTIONS)
    | HOW CAN I SLEEP BETTER
    | HOW TO IMPROVE MY SLEEP
    ;

// ----------------------------
// Help
// ----------------------------

helpCmd
    : HELP
    ;

// =====================================================
// Lexer Rules
// =====================================================

I           : 'i';
AM          : 'am';
IS          : 'is';

GOING       : 'going';
TO          : 'to';
SLEEP       : 'sleep';

WOKE        : 'woke';
UP          : 'up';
AWAKE       : 'awake';

WAKE        : 'wake';
ME          : 'me';
AT          : 'at';
IN          : 'in';

WARN        : 'warn';
IF          : 'if';
AFTER       : 'after';

WHAT        : 'what';
TIMEWORD    : 'time';
DID         : 'did';
YESTERDAY   : 'yesterday';

SHOW        : 'show';
CHECK       : 'check';
MY          : 'my';
CONSISTENCY : 'consistency';
REGULARITY  : 'regularity';
HOW         : 'how';
CONSISTENT  : 'consistent';
REGULAR     : 'regular';

HELP        : 'help';

CANCEL      : 'cancel';
STOP        : 'stop';
ALARM       : 'alarm';
SNOOZE      : 'snooze';
FOR         : 'for';

// Quality & Advice tokens
QUALITY     : 'quality';
RATE        : 'rate';
ANALYZE     : 'analyze';
GIVE        : 'give';
GET         : 'get';
ADVICE      : 'advice';
TIPS        : 'tips';
SUGGESTIONS : 'suggestions';
BETTER      : 'better';
IMPROVE     : 'improve';
CAN         : 'can';

// ----------------------------
// Time & Numbers
// ----------------------------

TIME
    : DIGIT DIGIT? ':' DIGIT DIGIT ('am' | 'pm')?
    | DIGIT DIGIT? ('am' | 'pm')
    ;

NUMBER
    : DIGIT+
    ;

TIMEUNIT
    : 'minute' | 'minutes' | 'hour' | 'hours'
    ;

fragment DIGIT : [0-9];

// ----------------------------
// Whitespace
// ----------------------------

WS : [ \t\r\n]+ -> skip;
