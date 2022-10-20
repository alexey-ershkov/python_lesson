from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 5000


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Simple server\n".encode('utf-8'))


server = HTTPServer(("localhost", PORT), HttpHandler)
print("Server started on port", PORT)

try:
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
