from telethon import TelegramClient
from telethon.tl.functions.payments import GetStarGiftsRequest
import asyncio

API_ID = 24526311        # <-- yahan apna API_ID
API_HASH = ""  # <-- yahan apna API_HASH
SESSION = ""

CHANNEL = "@fairyTailUpdates"

client = TelegramClient(SESSION, API_ID, API_HASH)

seen = set()

async def monitor():
    while True:
        result = await client(GetStarGiftsRequest(hash=0))

        for gift in result.gifts:
            if gift.id not in seen:
                seen.add(gift.id)

                msg = f"""🎁 New Gift Listing 🎁

🔗 {gift.slug}
💰 Price : {gift.price} ⭐️
"""
                await client.send_message(CHANNEL, msg)

        await asyncio.sleep(12)

async def main():
    await client.start()
    await monitor()

asyncio.run(main())
