import time
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

class SlowHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if urlparse(self.path).path == "/slow.js":
            time.sleep(1)

            self.send_response(200)
            self.send_header("Content-Type", "text/javascript")
            self.end_headers()
            self.wfile.write(bytes('console.log("slow.js is loaded");', 'utf-8'))
        else:
            self.send_response(404)


HTTPServer(("127.0.0.1", 9000), SlowHandler).serve_forever()
