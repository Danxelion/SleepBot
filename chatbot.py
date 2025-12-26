from antlr4 import *
from parser.SleepCommandsLexer import SleepCommandsLexer
from parser.SleepCommandsParser import SleepCommandsParser

from sleep_tracker import SleepTracker
from alarm_manager import AlarmManager
import re


class SleepBot:
    def __init__(self):
        self.tracker = SleepTracker()
        self.alarm = AlarmManager()

        # 🧠 Context memory
        self.last_intent = None
        self.last_alarm_time = None

    # --------------------------------------------------------
    # Text normalization (synonyms)
    # --------------------------------------------------------
    def normalize_text(self, text: str) -> str:
        text = text.lower().strip()

        synonyms = {
            "heading to bed": "going to sleep",
            "going to bed": "going to sleep",
            "about to sleep": "going to sleep",
            "turning in": "going to sleep",

            "i'm up": "i am awake",
            "im up": "i am awake",

            "wake me at": "wake me up at",
            "get me up at": "wake me up at",
            "set alarm for": "wake me up at",

            "alert me if": "warn me if",
            "notify me if": "warn me if",

            "when did i sleep last night": "what time did i sleep yesterday",
            
            # Quality synonyms
            "how well am i sleeping": "check my sleep quality",
            "how good is my sleep": "check my sleep quality",
            "sleep score": "check my sleep quality",
            "rate my sleep": "rate my sleep",
            
            # Advice synonyms
            "help me sleep better": "how can i sleep better",
            "sleep recommendations": "give me sleep advice",
            "what should i do": "give me advice"
        }

        for k, v in synonyms.items():
            if k in text:
                text = text.replace(k, v)

        return text

    # --------------------------------------------------------
    # Context follow-up (change alarm time)
    # --------------------------------------------------------
    def handle_context_followup(self, text: str):
        if self.last_intent == "set_alarm":
            match = re.search(r'(\d{1,2}(:\d{2})?\s?(am|pm)?)', text)
            if match:
                new_time = match.group(1)
                self.alarm.set_morning_alarm(new_time)
                self.last_alarm_time = new_time
                return f"⏰ Alarm updated to {new_time}"
        return None

    # --------------------------------------------------------
    # MAIN HANDLER
    # --------------------------------------------------------
    def handle(self, text: str) -> str:
        normalized = self.normalize_text(text)

        # 1️⃣ Parse with ANTLR FIRST
        input_stream = InputStream(normalized)
        lexer = SleepCommandsLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = SleepCommandsParser(tokens)

        try:
            tree = parser.command()
        except Exception:
            return "😕 Sorry, I didn’t quite understand that. Type *help* to see commands."

        child = tree.getChild(0)

        # ----------------------------------------------------
        # 🚨 Terminal alarm commands (bypass context follow-up)
        # ----------------------------------------------------
        if isinstance(child, SleepCommandsParser.CancelAlarmCmdContext):
            self.alarm.cancel_all()
            self.last_intent = None
            self.last_alarm_time = None
            return "⛔ Alarm canceled."

        if isinstance(child, SleepCommandsParser.SnoozeAlarmCmdContext):
            amount = int(child.NUMBER().getText())
            unit = child.TIMEUNIT().getText()

            minutes = amount * 60 if "hour" in unit else amount
            self.alarm.set_relative_alarm(minutes)
            self.last_intent = "snooze"

            return f"😴 Snoozing for {minutes} minutes."

        # ----------------------------------------------------
        # 2️⃣ Context follow-up (ONLY for alarm updates)
        # ----------------------------------------------------
        followup = self.handle_context_followup(normalized)
        if followup:
            return followup

        # --------------------
        # Sleep
        # --------------------
        if isinstance(child, SleepCommandsParser.SleepCmdContext):
            self.tracker.log_sleep()
            self.last_intent = "sleep"
            return "😴 Got it — sleep time logged. Good night!"

        # --------------------
        # Wake
        # --------------------
        if isinstance(child, SleepCommandsParser.WakeCmdContext):
            success, error = self.tracker.log_wake()
            self.last_intent = "wake"

            if not success:
                return f"⚠️ {error}"

            duration = self.tracker.get_last_sleep_duration()
            if duration:
                h, m = duration
                return (
                    "🌤️ Good morning!\n"
                    f"You slept for {h}h {m}m. Hope you feel rested!"
                )

            return "🌤️ Good morning! I’ve logged your wake-up time."

        # --------------------
        # Absolute alarm
        # --------------------
        if isinstance(child, SleepCommandsParser.SetAlarmCmdContext):
            t = child.TIME().getText()
            self.alarm.set_morning_alarm(t)

            self.last_intent = "set_alarm"
            self.last_alarm_time = t
            return f"⏰ All set! I’ll wake you up at {t}."

        # --------------------
        # Relative alarm
        # --------------------
        if isinstance(child, SleepCommandsParser.SetAlarmRelativeCmdContext):
            amount = int(child.NUMBER().getText())
            unit = child.TIMEUNIT().getText()

            minutes = amount * 60 if "hour" in unit else amount
            self.alarm.set_relative_alarm(minutes)

            self.last_intent = "set_alarm"
            return f"⏰ Done! I’ll wake you up in {minutes} minutes."

        # --------------------
        # Late alert
        # --------------------
        if isinstance(child, SleepCommandsParser.LateAlertCmdContext):
            t = child.TIME().getText()
            self.alarm.set_late_alert(t)

            self.last_intent = "late_alert"
            return f"⚠️ Okay! I’ll remind you if you’re still awake after {t}."

        # --------------------
        # Query
        # --------------------
        if isinstance(child, SleepCommandsParser.QueryCmdContext):
            t = self.tracker.get_yesterday_sleep_time()
            if not t:
                return "😕 I don’t have any sleep data yet. Try logging your sleep tonight!"
            return f"🕒 You went to sleep at {t}."

        # --------------------
        # Sleep consistency
        # --------------------
        if isinstance(child, SleepCommandsParser.ConsistencyCmdContext):
            stats = self.tracker.get_sleep_consistency()
            if not stats:
                return (
                    "📊 Sleep consistency report:\n"
                    "Not enough sleep data yet.\n"
                    "Log at least 2 complete sleep sessions."
                )

            bed_var = stats["bed_variance"]
            wake_var = stats["wake_variance"]

            if bed_var <= 30 and wake_var <= 30:
                rating = "Excellent 🟢"
            elif bed_var <= 60 and wake_var <= 60:
                rating = "Good 🟡"
            else:
                rating = "Poor 🔴"

            return (
                "📊 Sleep consistency report:\n"
                f"• Bedtime variation: {bed_var} minutes\n"
                f"• Wake-time variation: {wake_var} minutes\n"
                f"• Consistency rating: {rating}\n\n"
                "Tip: Try sleeping and waking within the same 30–60 minute window."
            )

        # --------------------
        # Sleep Quality
        # --------------------
        if isinstance(child, SleepCommandsParser.QualityCmdContext):
            quality = self.tracker.get_sleep_quality()
            if not quality:
                return (
                    "💤 Sleep Quality Report:\n"
                    "Not enough sleep data yet.\n"
                    "Log at least 1 complete sleep session."
                )
            
            score = quality["score"]
            rating = quality["rating"]
            emoji = quality["emoji"]
            avg_hours = quality["avg_duration_hours"]
            sessions = quality["sessions_analyzed"]
            
            response = f"{emoji} Sleep Quality Report:\n\n"
            response += f"🎯 Quality Score: {score}/100\n"
            response += f"⭐ Rating: {rating}\n"
            response += f"⏱️ Avg Duration: {avg_hours} hours\n"
            response += f"📅 Sessions Analyzed: {sessions}\n\n"
            
            if quality["positives"]:
                response += "✅ Positives:\n"
                for p in quality["positives"]:
                    response += f"  • {p}\n"
            
            if quality["issues"]:
                response += "\n⚠️ Areas to Improve:\n"
                for i in quality["issues"]:
                    response += f"  • {i}\n"
            
            response += "\nType 'give me advice' for personalized tips!"
            return response

        # --------------------
        # Sleep Advice
        # --------------------
        if isinstance(child, SleepCommandsParser.AdviceCmdContext):
            advice_data = self.tracker.get_sleep_advice()
            if not advice_data:
                return (
                    "💡 Sleep Advice:\n"
                    "I need more sleep data to give personalized advice.\n"
                    "Log a few sleep sessions first!"
                )
            
            score = advice_data["quality_score"]
            rating = advice_data["quality_rating"]
            items = advice_data["advice_items"]
            
            response = f"💡 Personalized Sleep Advice\n"
            response += f"Based on your sleep quality: {rating} ({score}/100)\n\n"
            
            for i, item in enumerate(items, 1):
                response += f"{item['icon']} {item['title']}\n"
                response += f"   {item['tip']}\n\n"
            
            return response.strip()

        # --------------------
        # Help
        # --------------------
        if isinstance(child, SleepCommandsParser.HelpCmdContext):
            return (
                "Here are some things you can try 😊\n\n"
                "📝 Logging:\n"
                "• I'm going to sleep\n"
                "• I am awake\n\n"
                "⏰ Alarms:\n"
                "• Wake me up at 7am\n"
                "• Wake me up in 5 minutes\n"
                "• Cancel alarm\n"
                "• Snooze for 5 minutes\n"
                "• Warn me if I am awake after 1am\n\n"
                "📊 Insights:\n"
                "• What time did I sleep yesterday\n"
                "• Show my sleep consistency\n"
                "• Check my sleep quality\n"
                "• Give me sleep advice"
            )

        return "😕 Sorry, I didn’t quite understand that. You can type *help* to see what I can do."


if __name__ == "__main__":
    bot = SleepBot()
    print("💤 SleepBot ready!")
    while True:
        user = input("You: ")
        print("Bot:", bot.handle(user))
