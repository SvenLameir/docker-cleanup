import os
import subprocess
import time

def prune_images():
    image_age = os.environ.get('IMAGE_AGE', '24h')
    print(f"Pruning images older than {image_age}...")
    try:
        subprocess.run([
            'docker', 'image', 'prune', '-a', '--force', f'--filter=until={image_age}'
        ], check=True)
    except FileNotFoundError:
        print("Error: Docker is not installed or not in PATH.")

def main():
    # How often to run the cleanup, in seconds (default: 3600 = 1 hour)
    run_interval = int(os.environ.get('RUN_INTERVAL', '3600'))

    while True:
        try:
            prune_images()
        except subprocess.CalledProcessError as e:
            print(f"Error during prune: {e}")
        # Wait before running again
        print(f"Sleeping for {run_interval} seconds...\n")
        time.sleep(run_interval)

if __name__ == "__main__":
    main()
