# Non-Stoppable Python 3 HTTP Server Example

A minimal Python 3 HTTP server that keeps running even when it receives graceful shutdown signals (`SIGTERM` / `SIGINT`). Useful for demonstrating long-running containerized processes.

## Requirements

- Python 3
- `make` (optional, for convenience)
- Docker (optional, for containerized run)

## Quick Start

Run locally:

```bash
make run
```

Or without `make`:

```bash
python3 server.py
```

The server listens on `0.0.0.0:8080` by default. Change the port with the `PORT` environment variable:

```bash
PORT=9000 python3 server.py
```

## Endpoints

| Method | Path      | Response                        |
|--------|-----------|---------------------------------|
| GET    | `/`       | `Hello, World!` (text/plain)    |
| GET    | `/health` | `{"status":"ok"}` (application/json) |
| *      | *         | `404 Not Found`                 |

## Testing

```bash
make test
```

This starts the server in the background, verifies both endpoints with `curl`, and then forcefully terminates the process.

## Docker

Build and run:

```bash
make docker-build
make docker-run
```

Stop the container:

```bash
make stop
```

## "Non-Stoppable" Behavior

The server registers handlers for `SIGTERM` and `SIGINT`. When either signal arrives, the handler logs the signal and returns, allowing the server to continue serving. The process exits only on `SIGKILL` or an unhandled fatal error.
