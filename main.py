from collector.network_collector import (
    collect_network_connections,
    save_connections_to_json
)


def main():
    print("[*] SentinelNode Phase 1 Collector Started")

    connections = collect_network_connections()
    save_connections_to_json(connections)

    print(f"[+] Collected {len(connections)} network connections")
    print("[+] Saved results to logs/network_connections.json")
    print("[*] SentinelNode Phase 1 Collector Finished")


if __name__ == "__main__":
    main()
