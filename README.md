# Docker Cleanup

This project provides a Docker container that removes old Docker images from the host system. The cleanup interval and image age are configurable via environment variables.

## Features
- Removes all unused Docker images older than a specified age (`IMAGE_AGE`, default: 24h)
- Configurable cleanup interval via the `RUN_INTERVAL` environment variable (supports units: s, m, h, d; default: 3600 seconds)
- Logs all actions and Docker output to the console
- Can be run manually or scheduled

## Usage

### Build the Docker Image
```sh
docker build -t cleanup:latest .
```

### Run the Container
```sh
docker run --rm \
  -e IMAGE_AGE=48h \
  -e RUN_INTERVAL=2h \
  -v /var/run/docker.sock:/var/run/docker.sock \
  cleanup:latest
```

- The `IMAGE_AGE` variable sets the age filter for image removal (e.g., `24h`, `48h`).
- The `RUN_INTERVAL` variable sets the interval between cleanup runs. You can use seconds (e.g., `3600`), minutes (`30m`), hours (`2h`), or days (`1d`).
- The Docker socket must be mounted for the container to manage images on the host.

### Example: Run Manually

You can also run the script directly on your host (requires Python 3 and Docker CLI):

```sh
export IMAGE_AGE=24h
export RUN_INTERVAL=1d
python cleanup.py
```

#### Supported RUN_INTERVAL Formats

- `3600`   → 3600 seconds (1 hour)
- `30m`    → 1800 seconds (30 minutes)
- `2h`     → 7200 seconds (2 hours)
- `1d`     → 86400 seconds (1 day)

## Logging

The script uses Python's built-in logging module. All actions, including Docker command output, are logged to the console with timestamps and log levels.

## License
Apache License 2.0
