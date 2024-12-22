import asyncio
import websockets
import json

async def connect_to_server_b():
    uri = "ws://localhost:8001/serverA"  # Connecting to Server B at the path /serverA
    async with websockets.connect(uri) as websocket:
        print("✅ Connected to Server B")

        # Sending a test message to Server B
        message_to_b = {
            "longitude": 11.564866,
            "latitude": 48.144463,
            "height": 4359.716,
            "heading": 360,
            "pitch": -90,
            "roll": 0
        }
        await websocket.send(json.dumps(message_to_b))
        print(f"📤 Sent message to Server B: {message_to_b}")

        # Receiving messages from Server B
        async for message in websocket:
            try:
                data = json.loads(message)
                print(f"📨 Received message from Server B: {data}")
            except json.JSONDecodeError:
                print("❌ Error decoding message")

async def main():
    await connect_to_server_b()

asyncio.run(main())
