import json
from pathlib import Path


LOG_DIR = Path("logs")
NETWORK_LOG_FILE = LOG_DIR / "network_connections.json"


def save_events_to_json(events, file_path=NETWORK_LOG_FILE):
    """
    Save SentinelNode events to a JSON file.

    Args:
        events (list): List of normalized SentinelNode events.
        file_path (Path): Output JSON file path.

    Returns:
        int: Number of events saved.
    """

    LOG_DIR.mkdir(exist_ok=True)

    with open(file_path, "w") as file:
        json.dump(events, file, indent=4)

    return len(events)
