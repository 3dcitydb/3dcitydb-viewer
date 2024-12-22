import asyncio
import websockets
import json

clients = {}
clients_lock = asyncio.Lock()

async def handler(websocket, path):
    global clients
    print(f"New connection on path: {path}")

    try:
        async with clients_lock:
            if path == "/serverA":
                clients['A'] = websocket
                print("✅ Server A connected")
            elif path == "/serverC":
                clients['C'] = websocket
                print("✅ Server C connected")
            else:
                await websocket.close()
                print("❌ Invalid path")
                return

        async for message in websocket:
            try:
                data = json.loads(message)
                print(f"📨 Received message from {path}: {data}")

                async with clients_lock:
                    if path == "/serverA" and 'C' in clients:
                        await clients['C'].send(json.dumps(data))
                        print("📤 Message forwarded to Server C")
                    elif path == "/serverC" and 'A' in clients:
                        await clients['A'].send(json.dumps(data))
                        print("📤 Message forwarded to Server A")
            except json.JSONDecodeError:
                print("❌ Error decoding message")

    except websockets.ConnectionClosed:
        print(f"🔌 Connection closed: {path}")
    finally:
        async with clients_lock:
            if path == "/serverA":
                clients.pop('A', None)
                print("❎ Server A disconnected")
            elif path == "/serverC":
                clients.pop('C', None)
                print("❎ Server C disconnected")

async def main():
    async with websockets.serve(handler, "localhost", 8001):
        print("✅ Server B is running on ws://localhost:8001")
        await asyncio.Future()  # Keeps the server running indefinitely

asyncio.run(main())
