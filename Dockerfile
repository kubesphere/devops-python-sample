FROM python:3-slim

WORKDIR /app

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

COPY server.py ./

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8080

ENV PORT=8080

CMD ["python", "server.py"]
