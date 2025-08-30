FROM python:3.11-alpine
ARG VERSION

# Install Docker CLI
RUN apk add --no-cache docker-cli

# Optionally set the cleanup interval (default is 24h)
ENV CLEANUP_INTERVAL=24h

# Add version label
LABEL org.opencontainers.image.version=$VERSION

COPY src/cleanup.py /cleanup.py
ENTRYPOINT ["python", "-m", "src.cleanup"]
