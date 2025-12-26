import threading
import time
from datetime import datetime


def normalize_time_string(t: str) -> str:
    """
    Converts '7am', '10:30pm', '06:15' → 'HH:MM'
    """
    t = t.strip().lower()

    is_pm = t.endswith("pm")
    is_am = t.endswith("am")

    if is_pm or is_am:
        t = t[:-2]

    if ":" in t:
        hour_str, minute_str = t.split(":")
    else:
        hour_str, minute_str = t, "00"

    hour = int(hour_str)
    minute = int(minute_str)

    if is_pm and hour != 12:
        hour += 12
    if is_am and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"


class AlarmManager:
    def __init__(self):
        self.absolute_alarm = None
        self.relative_timer = None
        self.late_alert_time = None

        threading.Thread(
            target=self._monitor_absolute,
            daemon=True
        ).start()

    # --------------------
    # Absolute alarm
    # --------------------
    def set_morning_alarm(self, time_str: str):
        self.absolute_alarm = normalize_time_string(time_str)
        print(f"[AlarmManager] Absolute alarm set for {self.absolute_alarm}")

    # --------------------
    # Relative alarm
    # --------------------
    def set_relative_alarm(self, minutes: int):
        if self.relative_timer:
            self.relative_timer.cancel()

        self.relative_timer = threading.Timer(
            minutes * 60,
            self._trigger_alarm
        )
        self.relative_timer.start()

        print(f"[AlarmManager] Relative alarm set for {minutes} minutes")

    # --------------------
    # Late-night alert
    # --------------------
    def set_late_alert(self, time_str: str):
        self.late_alert_time = normalize_time_string(time_str)
        print(f"[AlarmManager] Late alert set for {self.late_alert_time}")

    # --------------------
    # Alarm triggers
    # --------------------
    def _trigger_alarm(self):
        print("\n⏰ WAKE UP! (relative alarm)")
        self.relative_timer = None

    def _monitor_absolute(self):
        while True:
            now = datetime.now().strftime("%H:%M")

            if self.absolute_alarm == now:
                print(f"\n⏰ WAKE UP! It's {now}")
                self.absolute_alarm = None

            if self.late_alert_time == now:
                print(f"\n⚠️ You're still awake at {now}! Go to sleep!")
                self.late_alert_time = None

            time.sleep(30)

    # --------------------
    # Cancel ALL alarms
    # --------------------
    def cancel_all(self):
        if self.relative_timer:
            self.relative_timer.cancel()
            self.relative_timer = None

        self.absolute_alarm = None
        self.late_alert_time = None

        print("[AlarmManager] All alarms canceled")
