from collector.network_collector import (
    collect_network_connections,
    save_connections_to_json
)


def main():
    print("[*] SentinelNode Phase 2 Event Normalization Started")

    connections = collect_network_connections()
    save_connections_to_json(connections)

    print(f"[+] Collected and normalized {len(connections)} network connection events")
    print("[+] Saved normalized events to logs/network_connections.json")
    print("[*] SentinelNode Phase 2 Event Normalization Finished")


if __name__ == "__main__":
    main()
