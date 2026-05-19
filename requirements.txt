import requests
from bs4 import BeautifulSoup
import time

# =========================
# TELEGRAM SETTINGS
# =========================

BOT_TOKEN = "8873725770:AAHat5jB3WHBqdnOr8_4JdVPoM1OYl6S4O8"
CHANNEL_ID = "-1001813603496"

# =========================
# WEBSITE
# =========================

URL = "https://www.bitgetbuilder.com/"

# =========================
# LAST TASK STORAGE
# =========================

last_task = ""

# =========================
# SEND TELEGRAM MESSAGE
# =========================

def send_message(text):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.post(telegram_url, data=payload)

    print(response.text)

# =========================
# CHECK NEW TASK
# =========================

def check_task():

    global last_task

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(URL, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        # WEBSITE TASK TITLE
        task = soup.find("h3")

        if task:

            current_task = task.text.strip()

            if current_task != last_task:

                last_task = current_task

                message = f"""
🚨 NEW TASK LIVE

📌 {current_task}

⚡ FCFS Available
🎁 Reward Available

🔗 https://www.bitgetbuilder.com/
"""

                send_message(message)

                print("NEW TASK SENT")

            else:

                print("No new task")

    except Exception as e:

        print("ERROR:", e)

# =========================
# LOOP
# =========================

while True:

    check_task()

    # CHECK EVERY 5 MINUTES
    time.sleep(300)