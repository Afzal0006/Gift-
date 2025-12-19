import re
import math
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ===== CONFIG  =====
API_ID = 24526311
API_HASH = "717d5df262e474f88d86c537a787c98d"
SESSION = "BQF2PecANAmsjfKJkBv-PwZxQvinq0a7lcJ-6KCdyu13xnl8jeDV7YR9gk20ifB2M_7H2XqqUQMH0OAab9SXzfFqepsXHARqnp8JN7Iplo_5Odzwe6n5NBCFOyVP4Y3FGSdEQ4Y8UTM3VmCxTk8Jur_h9lCIKgxtLapFiiaYwgLwKWfP6W3XfsOs33FhjTEpHI8AOmZtqO4f5aAf3_2Mi032AHXKBDuzRqioX8RcG7JjYsjt-e8qnSudSpL20USBzR1FhGsYZjUx7W9_uPB7wjNH0P_6I3zJyynGPgdqIzkBi3sdZ2gRtgk7D-63t-jMbYuXIu5OfM6IZfCior4CVvRPu79nawAAAAHwVWW1AA"
OWNER_ID = 6998916494
# ================================

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)


ALLOWED = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}

def safe_eval(expr: str):
    code = compile(expr, "<calc>", "eval")
    for name in code.co_names:
        if name not in ALLOWED:
            raise ValueError("Invalid expression")
    return eval(code, {"__builtins__": {}}, ALLOWED)


MATH_REGEX = re.compile(r"^[0-9\.\+\-\*\/\%\(\) ]+$")

@client.on(events.NewMessage)
async def auto_calc(event):
    
    if event.sender_id != OWNER_ID:
        return

    text = event.raw_text.strip()

    if not text or len(text) > 50:
        return

    if MATH_REGEX.match(text):
        try:
            result = safe_eval(text)
            await event.reply(f"🧮 <b>Result:</b> <code>{result}</code>", parse_mode="html")
        except:
            pass

async def main():
    await client.start()
    await client.send_message(OWNER_ID, "💓 Calculator Userbot is alive!")
    print("✅ Calculator userbot running...")

client.loop.run_until_complete(main())
client.run_until_disconnected()
