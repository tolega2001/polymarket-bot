import asyncio
import websockets
import json

WS_URL = "wss://ws-clob.polymarket.com"

async def main():
    while True:
        try:
            async with websockets.connect(
                WS_URL,
                ping_interval=20,
                ping_timeout=20
            ) as ws:
                print("✅ Conectado a Polymarket")

                while True:
                    msg = await ws.recv()
                    data = json.loads(msg)
                    print(data)

        except Exception as e:
            print(f"⚠️ Conexión caída: {e}")
            print("🔄 Reintentando en 5 segundos...")
            await asyncio.sleep(5)

asyncio.run(main())




