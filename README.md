# Docker Cleanup Container

This project provides a Docker container that removes old Docker images from the host system. The cleanup interval is configurable via an environment variable.

## Features
- Removes all unused Docker images older than a specified interval (default: 24h)
- Configurable via the `CLEANUP_INTERVAL` environment variable (e.g., `12h`, `48h`)
- Can be run manually or scheduled
- Includes a GitHub Actions workflow to build and push the image to Docker Hub

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

- The `CLEANUP_INTERVAL` variable sets the age filter for image removal (default: 24h).
- The Docker socket must be mounted for the container to manage images on the host.

## GitHub Actions
A workflow is included at `.github/workflows/docker-build.yml` to build and push the image to Docker Hub on every push to the `main` branch.

Set the following secrets in your GitHub repository:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

## Files
- `cleanup.py`: Python script that performs the cleanup
- `Dockerfile`: Container definition
- `.github/workflows/docker-build.yml`: GitHub Actions workflow

## License
MIT
