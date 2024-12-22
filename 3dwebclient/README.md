# Demo Triangle Servers / Clients

```bash
A (Python Server) <-> B (Python Server) <-> C (Web App)
```

In this scenario:
+ `A` sends a message containing coordinates and camera settings for a location.
+ `B` forwards the message from `A` to `C` as well as from `C` back to `A` (middleware)
+ `C` changes the camera to the received coordinates and camera settings from `B` and sends a response to `B`

Steps:

```bash
# Clone the repository
git clone https://github.com/3dcitydb/3dcitydb-web-map
cd 3dcitydb-web-map

# Change branch
git checkout chat-web-triangle

# Change directory
cd 3dwebclient

# Install Python package
pip3 install websockets

# First, run the customized web client (on Windows)
python3 webApp.py
# Open http://localhost:8123/3dwebclient/ in browser

# Then, open a new console window and run B
python3 serverB.py

# Finally, open a new console window and run A
python3 serverA.py
# As soon as A starts, a message will be sent to B
# This message then be forwarded to C
# Switch to the web client in web browser and see the results
# Inspect the logs printed for A and B on the console
# Inspect logs for C by pressing F12 in browser
```
