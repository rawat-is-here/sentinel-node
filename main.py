from collector.network_collector import collect_network_connections
from sentinel_logger.json_logger import save_events_to_json


def main():
    print("[*] SentinelNode Phase 3 Logging Layer Started")

    events = collect_network_connections()
    saved_count = save_events_to_json(events)

    print(f"[+] Collected and normalized {len(events)} network connection events")
    print(f"[+] Saved {saved_count} events to logs/network_connections.json")
    print("[*] SentinelNode Phase 3 Logging Layer Finished")


if __name__ == "__main__":
    main()
