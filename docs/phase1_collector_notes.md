# SentinelNode Phase 1 — Network Collector Notes

## What this phase does

This phase collects active network connections from the endpoint.

The collector records:

- Timestamp
- Protocol family: IPv4 or IPv6
- Protocol: TCP or UDP
- Local IP address
- Local port
- Remote IP address
- Remote port
- Connection status
- PID
- Process name
- Process executable path

## Why this matters

Security analysts need endpoint telemetry to understand which processes are communicating over the network.

A network connection alone is not enough.

Example:

A connection to a public IP on port 443 may be normal if it comes from Chrome.

But the same type of connection may be suspicious if it comes from an unknown process running from `/tmp` or the Downloads folder.

## Current architecture

main.py starts the collector.

collector/network_collector.py collects network connection data.

logs/network_connections.json stores the collected telemetry.

## Current limitations

- No threat intelligence enrichment yet.
- No detection rules yet.
- No baseline comparison yet.
- No filtering of private/public IPs yet.
- No continuous monitoring yet.

## Next improvements

- Add hostname collection.
- Add process username.
- Add process creation time.
- Filter only external remote connections.
- Create structured event format.
- Later add detection and enrichment modules.
