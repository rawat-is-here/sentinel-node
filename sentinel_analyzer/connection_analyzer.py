def analyze_connections(events):
    """
    Analyze normalized SentinelNode network connection events.

    Args:
        events (list): List of normalized SentinelNode events.

    Returns:
        dict: Summary of connection activity.
    """

    summary = {
        "total_events": 0,
        "external_connections": 0,
        "internal_or_local_connections": 0,
        "listening_connections": 0,
        "established_connections": 0,
        "processes_with_external_connections": {},
        "remote_ports": {}
    }

    for event in events:
        summary["total_events"] += 1

        network = event.get("network", {})
        process = event.get("process", {})

        is_external = network.get("is_external_remote", False)
        status = network.get("status")
        remote_port = network.get("remote_port")
        process_name = process.get("name") or "unknown"

        if is_external:
            summary["external_connections"] += 1

            if process_name not in summary["processes_with_external_connections"]:
                summary["processes_with_external_connections"][process_name] = 0

            summary["processes_with_external_connections"][process_name] += 1
        else:
            summary["internal_or_local_connections"] += 1

        if status == "LISTEN":
            summary["listening_connections"] += 1

        if status == "ESTABLISHED":
            summary["established_connections"] += 1

        if remote_port is not None:
            port_key = str(remote_port)

            if port_key not in summary["remote_ports"]:
                summary["remote_ports"][port_key] = 0

            summary["remote_ports"][port_key] += 1

    return summary
