# Local static server for the site: python3 serve.py [port]
# Sturdier than `python3 -m http.server` behind tunnels: HTTP/1.1 keep-alive and a bigger connection queue.
import sys, http.server as h

class Handler(h.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

class Server(h.ThreadingHTTPServer):
    request_queue_size = 128
    daemon_threads = True

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8800
print(f"Serving on http://localhost:{port}")
Server(("", port), Handler).serve_forever()
