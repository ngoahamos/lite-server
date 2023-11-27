from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(post_data);
        # Handle the received data
        response_data = {'message': 'Received POST request', 'data': post_data}
        response_json = json.dumps(response_data).encode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', len(response_json))
        self.end_headers()

        self.wfile.write(response_json)

try:
    # Use port 8000, change it if needed
    port = 4500
    server_address = ('', port)

    with HTTPServer(server_address, MyHandler) as httpd:
        print(f'Starting server on port {port}')
        httpd.serve_forever()

except KeyboardInterrupt:
    print('Shutting down the server')
