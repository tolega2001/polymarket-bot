import asyncio
import websockets

WS_URL = "wss://ws.polymarket.com/ws"

async def main():
    async with websockets.connect(WS_URL) as ws:
        print("✅ Conectado a Polymarket")
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.run(main())



