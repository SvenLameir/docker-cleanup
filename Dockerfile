FROM python:3.11-alpine

# Install Docker CLI
RUN apk add --no-cache docker-cli

# Optionally set the cleanup interval (default is 24h)
ENV CLEANUP_INTERVAL=24h

COPY cleanup.py /cleanup.py
ENTRYPOINT ["python", "/cleanup.py"]
