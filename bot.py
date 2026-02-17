import asyncio
import websockets
import time

WS_URL = "wss://ws.polymarket.com"

async def run_bot():
    while True:
        try:
            print("🔌 Conectando a Polymarket...")
            async with websockets.connect(
                WS_URL,
                ping_interval=20,
                ping_timeout=20
            ) as ws:
                print("✅ Conectado a Polymarket")

                while True:
                    msg = await ws.recv()
                    print(msg)

        except Exception as e:
            print("⚠️ Conexión caída:", e)
            print("🔄 Reintentando en 5 segundos...")
            time.sleep(5)

asyncio.run(run_bot())




