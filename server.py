from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 80  # or 8080 if 80 is busy

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"\n[GET] Path: {self.path}")
        print(f"Client: {self.client_address[0]}")

        # Respond with 200 OK
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        return  # Disable default logging

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyHandler)
    print(f"Listening on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        server.server_close()
