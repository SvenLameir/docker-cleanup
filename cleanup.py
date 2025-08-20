import os
import subprocess

def main():
    # Get cleanup interval from environment variable, default to 24h
    cleanup_interval = os.environ.get('CLEANUP_INTERVAL', '24h')
    print(f"Pruning images older than {cleanup_interval}...")
    # Run the docker image prune command
    subprocess.run([
        'docker', 'image', 'prune', '-a', '--force', f'--filter=until={cleanup_interval}'
    ], check=True)

if __name__ == "__main__":
    main()
