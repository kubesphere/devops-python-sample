#!/usr/bin/env python3
"""A non-stoppable Python 3 HTTP server example."""

import json
import logging
import os
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DEFAULT_PORT = 8080


class RequestHandler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: bytes, content_type: str = "text/plain") -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/":
            self._send(200, b"Hello, World!\n")
        elif self.path == "/health":
            self._send(200, json.dumps({"status": "ok"}, separators=(",", ":")).encode(), "application/json")
        else:
            self._send(404, b"Not Found\n")

    def log_message(self, format: str, *args) -> None:  # noqa: A002
        logging.info("%s - %s", self.address_string(), format % args)


def _handle_signal(signum: int, frame) -> None:
    signal_name = signal.Signals(signum).name
    logging.info("Received %s; ignoring and continuing to serve.", signal_name)


def get_port() -> int:
    raw = os.environ.get("PORT", str(DEFAULT_PORT))
    try:
        return int(raw)
    except ValueError:
        logging.warning("Invalid PORT value %r; falling back to %d.", raw, DEFAULT_PORT)
        return DEFAULT_PORT


def main() -> int:
    port = get_port()
    server = HTTPServer(("0.0.0.0", port), RequestHandler)

    signal.signal(signal.SIGTERM, _handle_signal)
    signal.signal(signal.SIGINT, _handle_signal)

    logging.info("Starting non-stoppable server on 0.0.0.0:%d", port)
    try:
        server.serve_forever()
    except Exception as exc:  # noqa: BLE001
        logging.exception("Server failed: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
