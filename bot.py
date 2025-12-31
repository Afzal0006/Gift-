from telethon import TelegramClient
from telethon.tl.functions.payments import GetStarGiftsRequest
import asyncio

API_ID = 24526311        # <-- yahan apna API_ID
API_HASH = "717d5df262e474f88d86c537a787c98d"  # <-- yahan apna API_HASH
SESSION = "BQF2PecANAmsjfKJkBv-PwZxQvinq0a7lcJ-6KCdyu13xnl8jeDV7YR9gk20ifB2M_7H2XqqUQMH0OAab9SXzfFqepsXHARqnp8JN7Iplo_5Odzwe6n5NBCFOyVP4Y3FGSdEQ4Y8UTM3VmCxTk8Jur_h9lCIKgxtLapFiiaYwgLwKWfP6W3XfsOs33FhjTEpHI8AOmZtqO4f5aAf3_2Mi032AHXKBDuzRqioX8RcG7JjYsjt-e8qnSudSpL20USBzR1FhGsYZjUx7W9_uPB7wjNH0P_6I3zJyynGPgdqIzkBi3sdZ2gRtgk7D-63t-jMbYuXIu5OfM6IZfCior4CVvRPu79nawAAAAHwVWW1AA"

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
