import os
import requests
import time


TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TELEGRAM_TOKEN or not CHAT_ID:
    print("❌ Необхідно вказати TELEGRAM_BOT_TOKEN та TELEGRAM_CHAT_ID у змінних середовища.")
    exit(1)

def get_tunnel_url():
    try:
        resp = requests.get("http://ngrok:4040/api/tunnels")
        resp.raise_for_status()
        tunnels = resp.json().get("tunnels", [])
        for t in tunnels:
            if t.get("proto") == "tcp":
                return t.get("public_url")
    except Exception as e:
        print(f"⚠️  Помилка: {e}")
    return None


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        resp = requests.post(url, data=payload)
        resp.raise_for_status()
        print("📤 Повідомлення надіслано в Telegram")
    except Exception as e:
        print(f"❌ Не вдалося надіслати повідомлення: {e}")


print("⏳ Очікую на появу тунелю...")

for attempt in range(10):
    url = get_tunnel_url()
    url = url.replace("tcp://", "")

    if url:
        print(f"✅ Тунель знайдено: {url}")
        send_telegram_message(f"🎮 Minecraft доступний за адресою:\n\n{url}")
        break
    print(f"❌ Спроба {attempt + 1}: тунель ще не готовий")
    time.sleep(5)
else:
    print("🚫 Не вдалося знайти тунель після 10 спроб.")