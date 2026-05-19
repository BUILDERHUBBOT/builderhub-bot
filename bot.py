import requests
from bs4 import BeautifulSoup
import time

BOT_TOKEN = "8873725770:AAHat5jB3WHBqdnOr8_4JdVPoM1OYl6S4O8"
CHANNEL_ID = "-1001813603496"

URL = "https://www.bitgetbuilder.com/"

last_task = ""

def send_message(text):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    requests.post(telegram_url, data=payload)

def check_task():

    global last_task

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

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

while True:

    check_task()

    time.sleep(300)
