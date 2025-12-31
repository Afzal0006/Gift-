from telethon import TelegramClient
from telethon.tl.functions.payments import GetStarGiftsRequest
import asyncio

API_ID = 24526311        # <-- yahan apna API_ID
API_HASH = "717d5df262e474f88d86c537a787c98d"  # <-- yahan apna API_HASH
SESSION = "BQF2PecAeTUNNzoR0brOdxB_SQtDNxT-sOc1A1giDUQPANuGOoyNgNpQnnmnaWckd_MV4DPsdTAJFLtxsRcPBOuyt81hRaUX5J2ZVDLiA-Zb2ZwaoXkynFmNwzV6MHxEBEGU96aC91mGelD79eyXXTosavkb8EmzhGXkriF1hxGBcbI-cEfYQnNvkNyTr5vX-ZzDnE6lOsDzO_UnarAwqVpXyfdnNI5bdHf2blMQ2mCcVRS4wtFTBhYayhwEKFugYg3nWKdSbzDZ9x_AJ5ZVi_goMziq_flv2BWVg28pHOz4yVqBzxuluP7nc5etUX7TKwKFgu8rur7qJeLDV09iciAeZWxKEgAAAAHwVWW1AA"

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
