Quick 3-5 minute demo — SleepBot

Prep (30s)
- (Optional) Create & activate venv:

  python -m venv venv
  .\venv\Scripts\activate

- Install dependencies (if needed):

  python -m pip install flask antlr4-python3-runtime

- Start server (in project root):

  python server.py

Open http://127.0.0.1:5000 in a browser.

Demo timeline (3-5 minutes)
1. 00:00 — Landing page & stats (10s)
   - Verify landing page, night background and stats cards show.
   - Check chat icon (bottom-right) uses the custom image.

2. 00:10 — Open chat + quick sleep/wake sequence (60–90s)
   - Click chat icon to open the chat window.
   - Click Quick action: "😴 Sleep" (or type: "I'm going to sleep").
     Expected: Bot replies "sleep time logged".
   - Wait ~20–60s (short demo durations are fine).
   - Click Quick action: "🌤️ Wake" (or type: "I am awake").
     Expected: Bot replies with sleep duration (e.g. "You slept for 0h 1m").
   - Verify `data/sleep_log.json` now contains the new completed entry.

3. 01:40 — Repeat once more to create 2 short sessions (30–60s)
   - Log sleep, wake again quickly to produce 2 similar sessions.
   - Expected: Stats dashboard updates (Total Sessions increases).

4. 02:30 — Sleep Consistency check (20s)
   - In chat, type: "Show my sleep consistency" or click Stats quick action.
   - Expected: Report shows small "Bedtime variation" and "Wake-time variation" (minutes) and rating (Good/Excellent) because sessions are close in time.

5. 02:50 — Sleep Quality & Advice (30s)
   - Type: "Check my sleep quality" or "Rate my sleep".
     Expected: Score (0-100), rating and short positives/issues list.
   - Type: "Give me advice".
     Expected: Top 3–5 personalized tips (duration and consistency suggestions).

6. 03:20 — Alarm test (optional, 40s)
   - Type: "Wake me up in 1 minute".
     Expected: Server prints alarm trigger in terminal; client may show alarm modal if sound scheduled.
   - Type: "Cancel alarm" to test cancel behavior.
   - Type: "Snooze for 1 minute" to test relative alarm.

Quick verification checklist (during demo)
- Chat icon shows `chatbot-icon.png` image.
- Stats dashboard updates after each sleep/wake cycle.
- `sleep_log.json` correctly records `sleep` and `wake` timestamps.
- Consistency report reflects recent sessions (not large multi-hour numbers).
- Quality report contains a score, rating and items.
- Advice returns actionable tips prioritized by importance.
- Alarms log messages to the server terminal and relative alarms fire after the specified time.

Notes & troubleshooting
- If chat replies fail, check server terminal for stack traces.
- If Flask is missing: run `python -m pip install flask`.
- For ANTLR runtime import errors: run `python -m pip install antlr4-python3-runtime`.

That's it — a compact demo that exercises logging, stats, consistency, quality scoring and advice in ~3–5 minutes.