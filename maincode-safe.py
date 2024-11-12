import telegram
import random
import time
import schedule
from datetime import datetime, timedelta
import asyncio

bot_token = "YOUR_TOKEN"
bot = telegram.Bot(token=bot_token)

chat_id=YOUR_ID

def load_messages():
    with open("messages.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

async def send_random_message():
    messages = load_messages()
    if messages:
        message = random.choice(messages)
        await bot.send_message(chat_id=chat_id, text=message)
    schedule_random_message()

def schedule_random_message():
    delay_minutes = random.randint(10, 40)
    next_message_time = datetime.now() + timedelta(minutes=delay_minutes)
    print(f"Next message scheduled at: {next_message_time.strftime('%H:%M:%S')}")

    asyncio.get_event_loop().call_later(delay_minutes * 60, lambda: asyncio.create_task(send_random_message()))

async def main():
    # Schedule the first message
    schedule_random_message()

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
