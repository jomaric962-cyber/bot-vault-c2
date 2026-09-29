import os
from flask import Flask
from threading import Thread

# Ito ang "heartbeat" ng server para hindi i-shutdown ng Render
app = Flask(__name__)

@app.route('/')
def home():
    return "C2 Server is Active", 200

def run_bot():
    # Dito tatakbo ang Telegram Bot logic
    # Para sa initial deploy, hayaan muna nating tumakbo ang Flask
    pass

if __name__ == "__main__":
    # Render uses port 8080 or $PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    
    # Start bot in a separate thread
    t = Thread(target=run_bot)
    t.start()
    
    # Run Flask app
    app.run(host='0.0.0.0', port=port)