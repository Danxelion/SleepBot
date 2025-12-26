import json
import os
from datetime import datetime


class SleepTracker:
    FILE = os.path.join("data", "sleep_log.json")

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        try:
            with open(self.FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    # --------------------
    # Persistence
    # --------------------
    def save(self):
        with open(self.FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --------------------
    # Logging
    # --------------------
    def log_sleep(self):
        # Prevent double sleep
        if self.data and self.data[-1]["wake"] is None:
            return False, "You are already sleeping."

        self.data.append({
            "sleep": self.timestamp(),
            "wake": None
        })
        self.save()
        return True, None

    def log_wake(self):
        if not self.data:
            return False, "No sleep session found."

        if self.data[-1]["wake"] is not None:
            return False, "You already woke up."

        self.data[-1]["wake"] = self.timestamp()
        self.save()
        return True, None

    # --------------------
    # Queries
    # --------------------
    def get_yesterday_sleep_time(self):
        if not self.data:
            return None
        return self.data[-1]["sleep"]

    def _parse_time(self, t: str):
        return datetime.strptime(t, "%Y-%m-%d %H:%M:%S")

    def get_last_sleep_duration(self):
        if not self.data:
            return None

        last = self.data[-1]
        if last["sleep"] is None or last["wake"] is None:
            return None

        sleep_time = self._parse_time(last["sleep"])
        wake_time = self._parse_time(last["wake"])

        duration = wake_time - sleep_time
        total_minutes = int(duration.total_seconds() / 60)

        hours = total_minutes // 60
        minutes = total_minutes % 60
        return hours, minutes

    # --------------------
    # Consistency Analysis
    # --------------------
    def get_sleep_consistency(self):
        completed = [
            entry for entry in self.data
            if entry.get("sleep") and entry.get("wake")
        ]

        if len(completed) < 2:
            return None

        # Only use the last 7 entries for meaningful consistency analysis
        recent = completed[-7:]

        def minutes_from_midnight(dt):
            return dt.hour * 60 + dt.minute

        bedtimes = [minutes_from_midnight(self._parse_time(e["sleep"])) for e in recent]
        waketimes = [minutes_from_midnight(self._parse_time(e["wake"])) for e in recent]

        # Use standard deviation for more accurate variance measurement
        import statistics
        
        def circular_std(times):
            """Calculate variance for circular time data (handles midnight wrap)."""
            if len(times) < 2:
                return 0
            # Convert to radians (24h = 2π)
            import math
            radians = [t * 2 * math.pi / 1440 for t in times]
            # Calculate mean angle
            sin_sum = sum(math.sin(r) for r in radians)
            cos_sum = sum(math.cos(r) for r in radians)
            mean_angle = math.atan2(sin_sum, cos_sum)
            # Calculate angular differences
            diffs = []
            for r in radians:
                diff = r - mean_angle
                # Normalize to [-π, π]
                while diff > math.pi:
                    diff -= 2 * math.pi
                while diff < -math.pi:
                    diff += 2 * math.pi
                diffs.append(abs(diff))
            # Convert back to minutes
            avg_diff = sum(diffs) / len(diffs)
            return int(avg_diff * 1440 / (2 * math.pi))

        bed_variance = circular_std(bedtimes)
        wake_variance = circular_std(waketimes)
        
        # Calculate average bedtime for display
        avg_bedtime = sum(bedtimes) / len(bedtimes)

        return {
            "avg_bedtime": avg_bedtime,
            "bed_variance": bed_variance,
            "wake_variance": wake_variance,
            "sessions_analyzed": len(recent)
        }

    # --------------------
    # Statistics for UI
    # --------------------
    def get_statistics(self):
        """Get sleep statistics for the dashboard."""
        completed = [
            entry for entry in self.data
            if entry.get("sleep") and entry.get("wake")
        ]
        
        if not completed:
            return None
        
        # Calculate total sleep sessions
        total_sessions = len(completed)
        
        # Calculate average sleep duration
        durations = []
        for entry in completed:
            sleep_time = self._parse_time(entry["sleep"])
            wake_time = self._parse_time(entry["wake"])
            duration_mins = (wake_time - sleep_time).total_seconds() / 60
            if duration_mins > 0:
                durations.append(duration_mins)
        
        avg_duration = sum(durations) / len(durations) if durations else 0
        avg_hours = int(avg_duration // 60)
        avg_mins = int(avg_duration % 60)
        
        # Last sleep info
        last = completed[-1]
        last_sleep = self._parse_time(last["sleep"])
        last_wake = self._parse_time(last["wake"])
        last_duration = (last_wake - last_sleep).total_seconds() / 60
        last_hours = int(last_duration // 60)
        last_mins = int(last_duration % 60)
        
        # Best sleep (longest duration)
        best_duration = max(durations) if durations else 0
        best_hours = int(best_duration // 60)
        best_mins = int(best_duration % 60)
        
        return {
            "total_sessions": total_sessions,
            "avg_duration": f"{avg_hours}h {avg_mins}m",
            "last_duration": f"{last_hours}h {last_mins}m",
            "best_duration": f"{best_hours}h {best_mins}m",
            "last_sleep_time": last_sleep.strftime("%I:%M %p"),
            "last_wake_time": last_wake.strftime("%I:%M %p")
        }

    # --------------------
    # Sleep Quality Analysis
    # --------------------
    def get_sleep_quality(self):
        """Analyze sleep quality based on duration, consistency, and patterns."""
        completed = [
            entry for entry in self.data
            if entry.get("sleep") and entry.get("wake")
        ]
        
        if not completed:
            return None
        
        # Use last 7 sessions for analysis
        recent = completed[-7:]
        
        # Calculate durations
        durations = []
        for entry in recent:
            sleep_time = self._parse_time(entry["sleep"])
            wake_time = self._parse_time(entry["wake"])
            duration_mins = (wake_time - sleep_time).total_seconds() / 60
            if duration_mins > 0:
                durations.append(duration_mins)
        
        if not durations:
            return None
        
        avg_duration_mins = sum(durations) / len(durations)
        avg_hours = avg_duration_mins / 60
        
        # Quality scoring (0-100)
        quality_score = 0
        issues = []
        positives = []
        
        # 1. Duration score (40 points max)
        # Optimal: 7-9 hours
        if 420 <= avg_duration_mins <= 540:  # 7-9 hours
            quality_score += 40
            positives.append("Great sleep duration (7-9 hours)")
        elif 360 <= avg_duration_mins < 420:  # 6-7 hours
            quality_score += 30
            issues.append("Slightly short sleep (6-7 hours)")
        elif 540 < avg_duration_mins <= 600:  # 9-10 hours
            quality_score += 30
            issues.append("Slightly long sleep (9-10 hours)")
        elif 300 <= avg_duration_mins < 360:  # 5-6 hours
            quality_score += 15
            issues.append("Short sleep duration (5-6 hours)")
        elif avg_duration_mins > 600:  # >10 hours
            quality_score += 15
            issues.append("Oversleeping (>10 hours)")
        else:  # <5 hours
            quality_score += 5
            issues.append("Very short sleep (<5 hours)")
        
        # 2. Consistency score (30 points max)
        consistency = self.get_sleep_consistency()
        if consistency:
            bed_var = consistency["bed_variance"]
            wake_var = consistency["wake_variance"]
            
            if bed_var <= 30 and wake_var <= 30:
                quality_score += 30
                positives.append("Excellent sleep schedule consistency")
            elif bed_var <= 60 and wake_var <= 60:
                quality_score += 20
                positives.append("Good sleep schedule consistency")
            elif bed_var <= 90 and wake_var <= 90:
                quality_score += 10
                issues.append("Inconsistent sleep schedule")
            else:
                quality_score += 5
                issues.append("Very irregular sleep schedule")
        
        # 3. Regularity score (30 points max) - based on number of sessions
        sessions_count = len(recent)
        if sessions_count >= 7:
            quality_score += 30
            positives.append("Regular sleep tracking")
        elif sessions_count >= 5:
            quality_score += 20
            positives.append("Fairly regular tracking")
        elif sessions_count >= 3:
            quality_score += 10
            issues.append("Inconsistent tracking")
        else:
            quality_score += 5
            issues.append("Very few sleep records")
        
        # Determine rating
        if quality_score >= 80:
            rating = "Excellent 🌟"
            emoji = "😴💪"
        elif quality_score >= 60:
            rating = "Good 😊"
            emoji = "😴👍"
        elif quality_score >= 40:
            rating = "Fair 😐"
            emoji = "😴"
        else:
            rating = "Needs Improvement 😟"
            emoji = "😴⚠️"
        
        return {
            "score": quality_score,
            "rating": rating,
            "emoji": emoji,
            "avg_duration_hours": round(avg_hours, 1),
            "sessions_analyzed": len(recent),
            "issues": issues,
            "positives": positives
        }

    # --------------------
    # Sleep Advice
    # --------------------
    def get_sleep_advice(self):
        """Generate personalized sleep advice based on quality and consistency."""
        quality = self.get_sleep_quality()
        consistency = self.get_sleep_consistency()
        
        if not quality:
            return None
        
        advice = []
        
        # Duration-based advice
        avg_hours = quality["avg_duration_hours"]
        if avg_hours < 6:
            advice.append({
                "priority": "high",
                "icon": "⚠️",
                "title": "Increase Sleep Duration",
                "tip": "Aim for 7-9 hours of sleep. Try going to bed 30 minutes earlier each night until you reach your goal."
            })
        elif avg_hours < 7:
            advice.append({
                "priority": "medium",
                "icon": "💡",
                "title": "Slightly Increase Sleep Time",
                "tip": "You're close! Try adding 30-60 minutes to your sleep for optimal rest."
            })
        elif avg_hours > 10:
            advice.append({
                "priority": "medium",
                "icon": "💡",
                "title": "Consider Reducing Sleep Time",
                "tip": "Oversleeping can cause grogginess. Try setting an alarm and maintaining a consistent wake time."
            })
        else:
            advice.append({
                "priority": "low",
                "icon": "✅",
                "title": "Great Sleep Duration",
                "tip": "Keep up the good work! Your sleep duration is in the healthy range."
            })
        
        # Consistency-based advice
        if consistency:
            bed_var = consistency["bed_variance"]
            wake_var = consistency["wake_variance"]
            
            if bed_var > 60:
                advice.append({
                    "priority": "high",
                    "icon": "🕐",
                    "title": "Stabilize Your Bedtime",
                    "tip": f"Your bedtime varies by ~{bed_var} minutes. Try going to bed within the same 30-minute window each night."
                })
            
            if wake_var > 60:
                advice.append({
                    "priority": "high",
                    "icon": "🌅",
                    "title": "Consistent Wake Time",
                    "tip": f"Your wake time varies by ~{wake_var} minutes. A consistent wake time helps regulate your body clock."
                })
            
            if bed_var <= 30 and wake_var <= 30:
                advice.append({
                    "priority": "low",
                    "icon": "🎯",
                    "title": "Excellent Consistency",
                    "tip": "Your sleep schedule is very consistent. This helps maintain a healthy circadian rhythm!"
                })
        
        # General tips based on score
        if quality["score"] < 60:
            advice.append({
                "priority": "medium",
                "icon": "📱",
                "title": "Create a Bedtime Routine",
                "tip": "Avoid screens 1 hour before bed, keep your room cool and dark, and try relaxation techniques."
            })
            advice.append({
                "priority": "medium",
                "icon": "☕",
                "title": "Watch Your Caffeine",
                "tip": "Avoid caffeine at least 6 hours before bedtime for better sleep quality."
            })
        
        if quality["sessions_analyzed"] < 5:
            advice.append({
                "priority": "medium",
                "icon": "📊",
                "title": "Track More Consistently",
                "tip": "Log your sleep daily for more accurate insights and personalized recommendations."
            })
        
        # Sort by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        advice.sort(key=lambda x: priority_order[x["priority"]])
        
        return {
            "quality_score": quality["score"],
            "quality_rating": quality["rating"],
            "advice_items": advice[:5]  # Top 5 advice items
        }
