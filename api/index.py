from http.server import BaseHTTPRequestHandler
import json
import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = self._generate_response()
        self._send_response(200, response)

    def _generate_response(self):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response = {
            'message': 'Hello, world!',
            'current_time': current_time
        }
        return json.dumps(response)

    def _send_response(self, status_code, response):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))