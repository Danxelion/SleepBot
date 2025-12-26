// ============================
// Alarm sound
// ============================
const alarmSound = new Audio("/sound/myinstants.mp3");
alarmSound.loop = true;

// ============================
// Active alarm tracking
// ============================
let activeAlarmTimeout = null;

// ============================
// Chat toggle
// ============================
const chatWindow = document.getElementById("chat-window");
const chatToggle = document.getElementById("chat-toggle");
const chatClose = document.getElementById("chat-close");

chatToggle.addEventListener("click", () => {
    chatWindow.classList.toggle("hidden");
});

chatClose.addEventListener("click", () => {
    chatWindow.classList.add("hidden");
});

// ============================
// Message bubbles
// ============================
function addMessage(text, sender = "bot") {
    const box = document.getElementById("chat-box");

    const row = document.createElement("div");
    row.className = "message-row " + sender;

    const bubble = document.createElement("div");
    bubble.className = "message-bubble";

    bubble.innerHTML = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/\n/g, "<br>");

    row.appendChild(bubble);
    box.appendChild(row);

    box.scrollTop = box.scrollHeight;
}

// ============================
// Typing indicator
// ============================
let typingIndicator = null;

function showTypingIndicator() {
    const box = document.getElementById("chat-box");

    typingIndicator = document.createElement("div");
    typingIndicator.className = "message-row bot typing";
    typingIndicator.textContent = "SleepBot is typing…";

    box.appendChild(typingIndicator);
    box.scrollTop = box.scrollHeight;
}

function hideTypingIndicator() {
    if (typingIndicator) {
        typingIndicator.remove();
        typingIndicator = null;
    }
}

// ============================
// Send message
// ============================
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;

    addMessage(message, "user");
    input.value = "";

    showTypingIndicator();

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
        .then(res => res.json())
        .then(data => {
            hideTypingIndicator();
            addMessage(data.reply, "bot");

            // 🔔 Detect alarm from bot reply
            detectAndScheduleAlarm(data.reply);
        })
        .catch(() => {
            hideTypingIndicator();
            addMessage("⚠️ Server error. Please try again.", "bot");
        });
}

document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keydown", e => {
    if (e.key === "Enter") sendMessage();
});

// ============================
// Initial message
// ============================
window.addEventListener("load", () => {
    addMessage(
        "Hello! I'm SleepBot 😴\nTry:\n• I'm going to sleep\n• Wake me up at 7am\n• Wake me up in 5 minutes\n• Show my sleep consistency",
        "bot"
    );
});

// ============================
// Alarm detection logic
// ============================
function detectAndScheduleAlarm(reply) {

    // ⛔ Cancel alarm
    if (/alarm canceled/i.test(reply)) {
        clearActiveAlarm();
        return;
    }

    // 😴 Snooze alarm
    const snoozeMatch = reply.match(/snoozing for (\d+)\s+minutes/i);
    if (snoozeMatch) {
        const minutes = parseInt(snoozeMatch[1]);
        scheduleRelativeAlarm(minutes);
        return;
    }

    // 🔔 Relative alarm
    const relativeMatch = reply.match(/wake you up in (\d+)\s+minutes?/i);
    if (relativeMatch) {
        const minutes = parseInt(relativeMatch[1]);
        scheduleRelativeAlarm(minutes);
        return;
    }

    // ⏰ Absolute alarm
    const absoluteMatch = reply.match(/wake you up at ([0-9:]+ ?(am|pm)?)/i);
    if (absoluteMatch) {
        scheduleAbsoluteAlarm(absoluteMatch[1]);
    }
}

// ============================
// Absolute alarm
// ============================
function scheduleAbsoluteAlarm(timeStr) {
    clearActiveAlarm();

    const now = new Date();
    const target = new Date();

    const match = timeStr.match(/(\d{1,2})(:(\d{2}))?\s?(am|pm)?/i);
    if (!match) return;

    let hour = parseInt(match[1]);
    let minute = match[3] ? parseInt(match[3]) : 0;
    const ampm = match[4];

    if (ampm === "pm" && hour !== 12) hour += 12;
    if (ampm === "am" && hour === 12) hour = 0;

    target.setHours(hour, minute, 0, 0);

    if (target <= now) {
        target.setDate(target.getDate() + 1);
    }

    const delay = target - now;
    activeAlarmTimeout = setTimeout(triggerAlarm, delay);
}

// ============================
// Relative alarm
// ============================
function scheduleRelativeAlarm(minutes) {
    clearActiveAlarm();
    activeAlarmTimeout = setTimeout(
        triggerAlarm,
        minutes * 60 * 1000
    );
}

// ============================
// Clear alarm
// ============================
function clearActiveAlarm() {
    if (activeAlarmTimeout) {
        clearTimeout(activeAlarmTimeout);
        activeAlarmTimeout = null;
    }
    stopAlarm();
}

// ============================
// Alarm trigger
// ============================
function triggerAlarm() {
    alarmSound.play();
    document.getElementById("alarm-modal").classList.remove("hidden");
}

function stopAlarm() {
    alarmSound.pause();
    alarmSound.currentTime = 0;
    document.getElementById("alarm-modal").classList.add("hidden");
}

// ============================
// Quick actions
// ============================
function quickSend(text) {
    document.getElementById("user-input").value = text;
    sendMessage();
}

// ============================
// Statistics Dashboard
// ============================
function loadStatistics() {
    fetch("/stats")
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                console.log("No stats available yet");
                return;
            }
            
            // Update stat cards
            document.getElementById("stat-sessions").textContent = data.total_sessions || "-";
            document.getElementById("stat-avg").textContent = data.avg_duration || "-";
            document.getElementById("stat-best").textContent = data.best_duration || "-";
            document.getElementById("stat-last").textContent = data.last_duration || "-";
            
            // Update last activity
            document.getElementById("last-sleep-time").textContent = data.last_sleep_time || "--";
            document.getElementById("last-wake-time").textContent = data.last_wake_time || "--";
        })
        .catch(err => {
            console.log("Could not load statistics:", err);
        });
}

// Load statistics on page load
document.addEventListener("DOMContentLoaded", loadStatistics);

// Refresh statistics after each message (in case sleep/wake was logged)
const originalSendMessage = sendMessage;
sendMessage = function() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;

    addMessage(message, "user");
    input.value = "";

    showTypingIndicator();

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
        .then(res => res.json())
        .then(data => {
            hideTypingIndicator();
            addMessage(data.reply, "bot");

            // 🔔 Detect alarm from bot reply
            detectAndScheduleAlarm(data.reply);
            
            // 📊 Refresh statistics after action
            loadStatistics();
        })
        .catch(() => {
            hideTypingIndicator();
            addMessage("⚠️ Failed to send message.", "bot");
        });
};
