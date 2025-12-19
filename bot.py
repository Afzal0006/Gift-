import asyncio
from datetime import datetime

from telethon import TelegramClient
from telethon.sessions import StringSession

import aiohttp
from bs4 import BeautifulSoup

# ===== CONFIG =====
API_ID = 24526311        # your api_id
API_HASH = "717d5df262e474f88d86c537a787c98d" # your api_hash
SESSION = "BQF2PecANAmsjfKJkBv-PwZxQvinq0a7lcJ-6KCdyu13xnl8jeDV7YR9gk20ifB2M_7H2XqqUQMH0OAab9SXzfFqepsXHARqnp8JN7Iplo_5Odzwe6n5NBCFOyVP4Y3FGSdEQ4Y8UTM3VmCxTk8Jur_h9lCIKgxtLapFiiaYwgLwKWfP6W3XfsOs33FhjTEpHI8AOmZtqO4f5aAf3_2Mi032AHXKBDuzRqioX8RcG7JjYsjt-e8qnSudSpL20USBzR1FhGsYZjUx7W9_uPB7wjNH0P_6I3zJyynGPgdqIzkBi3sdZ2gRtgk7D-63t-jMbYuXIu5OfM6IZfCior4CVvRPu79nawAAAAHwVWW1AA"  # or leave empty to login first time

OWNER_ID = 6998916494  # your Telegram user id
CHECK_EVERY = 3     # seconds

MARKET_URL = "https://marketapp.ws/gifts/?tab=history"
# ==================

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

last_seen = set()

async def fetch_sales():
    sales = []
    async with aiohttp.ClientSession() as session:
        async with session.get(MARKET_URL, timeout=20) as r:
            html = await r.text()

    soup = BeautifulSoup(html, "html.parser")

    # ⚠️ This selector is example – site ke HTML ke hisaab se change karna padega
    rows = soup.select(".history-item")
    for row in rows[:10]:
        name = row.select_one(".gift-name").get_text(strip=True)
        price = row.select_one(".price").get_text(strip=True).replace("⭐", "")
        uid = row.get("data-id", f"{name}-{price}")
        sales.append((uid, name, price))

    return sales

async def monitor():
    await client.start()

    # 🔔 Alive message on start
    await client.send_message(
        OWNER_ID,
        "💓 Alive! NFT Sale Userbot is now running."
    )

    print("✅ Bot started and alive message sent")

    while True:
        try:
            sales = await fetch_sales()
            for uid, name, price in sales:
                if uid not in last_seen:
                    last_seen.add(uid)

                    msg = (
                        "🎁 <b>Gift Sold!</b>\n"
                        f"⭐ <b>{name}</b>\n"
                        f"💰 Price: {price}\n"
                        f"🕒 Time: Now"
                    )
                    await client.send_message(OWNER_ID, msg, parse_mode="html")

            await asyncio.sleep(CHECK_EVERY)

        except Exception as e:
            print("Error:", e)
            await asyncio.sleep(10)
