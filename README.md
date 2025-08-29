# Docker Cleanup Container

This project provides a Docker container that removes old Docker images from the host system. The cleanup interval is configurable via an environment variable.

## Features
- Removes all unused Docker images older than a specified age `IMAGE_AGE`(default: 24h)
- Configurable via the `RUN_INTERVAL` environment variable (e.g., `12h`, `48h`)
- Can be run manually or scheduled

## Usage

### Build the Docker Image
```
docker build -t cleanup:latest .
```

### Run the Container
```
docker run --rm \
  -e CLEANUP_INTERVAL=48h \
  -v /var/run/docker.sock:/var/run/docker.sock \
  cleanup:latest
```

- The `IMAGE_AGE` variable sets the age filter for image removal (default: 24h).
- The `RUN_INTERVAL` variable sets the interval on which images are removed (default: 1h). 
- The Docker socket must be mounted for the container to manage images on the host.

## License
MIT
