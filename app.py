from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from io import BytesIO
from random import randint
from base64 import encode

import redis
import os


r = redis.from_url(os.getenv("REDIS_URL", "redis://127.0.0.1:6379"))


class Random(BaseHTTPRequestHandler):
    def do_GET(self):
        print(Path(__file__).resolve().parent)
        file_path = str(Path(__file__).resolve().parent) + "/" + "index.html"
        html = open(file_path, 'rb')

        self.send_response(200)

        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(html.read())
    
    def do_POST(self):
        name = randint(60000, 99999)
        r.set(name, "crap")

        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Number of craps: ')
        response.write(str(r.dbsize()).encode())

        self.wfile.write(response.getvalue())


if __name__ == "__main__":
    server_address = ('', 6503)
    httpd = HTTPServer(server_address, Random)
    httpd.serve_forever()