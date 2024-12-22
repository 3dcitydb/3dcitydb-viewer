import http.server
import socketserver
import os

# Define the port for the server
PORT = 8123

# Set the directory where your static files (e.g., index.html) are located
WEB_DIRECTORY = ".."

# Change the working directory to the location of the index.html
os.chdir(WEB_DIRECTORY)

# Set up the request handler to serve files in the directory
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving files from {WEB_DIRECTORY} at http://localhost:{PORT}")
    httpd.serve_forever()
