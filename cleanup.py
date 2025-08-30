import os
import subprocess
import time
import logging

def prune_images(image_age: str = '24h') -> None:
    """
    Prune Docker images older than the specified age and log the output.
    Args:
        image_age (str): Age filter for images to prune (e.g., '24h').
    """
    # Log the start of the prune operation
    logging.info(f"Pruning images older than {image_age}...")
    try:
        # Run the docker image prune command and capture output
        result = subprocess.run([
            'docker', 'image', 'prune', '-a', '--force', f'--filter=until={image_age}'
        ], check=True, capture_output=True, text=True)
        logging.info("Image prune completed successfully.")
        # Log standard output from the command
        if result.stdout:
            logging.info(f"docker output:\n{result.stdout}")
        # Log any error output from the command
        if result.stderr:
            logging.warning(f"docker error output:\n{result.stderr}")
    except FileNotFoundError:
        # Handle case where Docker is not installed
        logging.error("Docker is not installed or not in PATH.")
    except subprocess.CalledProcessError as e:
        # Handle errors from the docker command
        logging.error(f"Error during prune: {e}")
        if e.stdout:
            logging.error(f"docker output:\n{e.stdout}")
        if e.stderr:
            logging.error(f"docker error output:\n{e.stderr}")

def get_env_variable(name: str, default: str) -> str:
    """
    Get an environment variable or return a default value.
    Args:
        name (str): The environment variable name.
        default (str): The default value if the variable is not set.
    Returns:
        str: The value of the environment variable or the default.
    """
    return os.environ.get(name, default)

import re

def parse_interval(interval_str: str) -> int:
    """
    Parse a time interval string (e.g., '2h', '30m', '1d', '3600') into seconds.
    Supported units: s (seconds), m (minutes), h (hours), d (days).
    If no unit is given, seconds are assumed.
    """
    interval_str = interval_str.strip().lower()
    match = re.fullmatch(r"(\d+)([smhd]?)", interval_str)
    if not match:
        raise ValueError(f"Invalid interval format: {interval_str}")
    value, unit = match.groups()
    value = int(value)
    if unit == '':
        return value
    elif unit == 's':
        return value
    elif unit == 'm':
        return value * 60
    elif unit == 'h':
        return value * 3600
    elif unit == 'd':
        return value * 86400
    else:
        raise ValueError(f"Unknown time unit: {unit}")

def main() -> None:
    """
    Main loop to periodically prune Docker images.
    """
    # Configure logging format and level
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Get image age and run interval from environment variables
    image_age = get_env_variable('IMAGE_AGE', '24h')
    run_interval_str = get_env_variable('RUN_INTERVAL', '3600')
    try:
        run_interval = parse_interval(run_interval_str)
    except ValueError:
        # Handle invalid interval value
        logging.warning(f"Invalid RUN_INTERVAL '{run_interval_str}', using default 3600 seconds.")
        run_interval = 3600

    # Main loop: prune images and sleep for the interval
    while True:
        prune_images(image_age)
        logging.info(f"Sleeping for {run_interval} seconds...\n")
        time.sleep(run_interval)

if __name__ == "__main__":
    main()
