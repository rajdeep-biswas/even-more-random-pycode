from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        f = open('example.html', 'r')
        html = bytes(f.read(), 'utf-8')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html)

port = 8000
serverIp = ("0.0.0.0", port)
server = HTTPServer(serverIp, HTTPServer_RequestHandler)
server.serve_forever()
