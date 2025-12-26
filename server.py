from flask import Flask, request, jsonify
from chatbot import SleepBot
import traceback

app = Flask(__name__, static_url_path='', static_folder='static')
bot = SleepBot()


# -----------------------------
# Serve frontend
# -----------------------------
@app.route("/")
def home():
    return app.send_static_file("index.html")


# -----------------------------
# Chat API (SAFE)
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)

        if not data or "message" not in data:
            return jsonify({
                "reply": "⚠️ Invalid request format."
            }), 400

        user_msg = data["message"].strip()
        if not user_msg:
            return jsonify({
                "reply": "⚠️ Please type a message."
            })

        reply = bot.handle(user_msg)

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        # 🔥 Log full traceback to terminal
        print("❌ SERVER ERROR:")
        traceback.print_exc()

        # ✅ Always return JSON (never HTML)
        return jsonify({
            "reply": "⚠️ Something went wrong on the server. Please try again."
        }), 500


# -----------------------------
# Statistics API
# -----------------------------
@app.route("/stats", methods=["GET"])
def get_stats():
    try:
        stats = bot.tracker.get_statistics()
        if stats:
            return jsonify(stats)
        return jsonify({"error": "No data available"})
    except Exception as e:
        print("❌ STATS ERROR:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
