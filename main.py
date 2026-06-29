from collector.network_collector import collect_network_connections
from sentinel_logger.json_logger import save_events_to_json
from sentinel_analyzer.connection_analyzer import analyze_connections


def print_analysis_summary(summary):
    print("\n[*] SentinelNode Connection Analysis Summary")
    print(f"[+] Total events: {summary['total_events']}")
    print(f"[+] External connections: {summary['external_connections']}")
    print(f"[+] Internal/local connections: {summary['internal_or_local_connections']}")
    print(f"[+] Listening connections: {summary['listening_connections']}")
    print(f"[+] Established connections: {summary['established_connections']}")

    print("\n[*] Processes with external connections:")
    if summary["processes_with_external_connections"]:
        for process_name, count in summary["processes_with_external_connections"].items():
            print(f"    - {process_name}: {count}")
    else:
        print("    - None")

    print("\n[*] Remote ports observed:")
    if summary["remote_ports"]:
        for port, count in summary["remote_ports"].items():
            print(f"    - Port {port}: {count}")
    else:
        print("    - None")


def main():
    print("[*] SentinelNode Phase 4 Connection Analysis Started")

    events = collect_network_connections()
    saved_count = save_events_to_json(events)
    summary = analyze_connections(events)

    print(f"[+] Collected and normalized {len(events)} network connection events")
    print(f"[+] Saved {saved_count} events to logs/network_connections.json")

    print_analysis_summary(summary)

    print("\n[*] SentinelNode Phase 4 Connection Analysis Finished")


if __name__ == "__main__":
    main()
