SentinelNode — Endpoint Telemetry & Threat Detection Agent

SentinelNode is a defensive cybersecurity learning project that simulates the early foundation of a lightweight Endpoint Detection and Response system.

The project collects endpoint network telemetry, enriches it with process context, converts it into a normalized event format, and stores it as structured JSON logs.

This project is being built step by step to understand how endpoint telemetry, detection engineering, threat intelligence enrichment, baselining, and SIEM-style logging work in real security environments.

---

Current Phase

Phase 3 — Logging Layer

The current version collects active network connections from the local machine, enriches them with process context, converts them into normalized SentinelNode events, and saves the final output through a dedicated JSON logging layer.

The project now separates collection, formatting, and logging into different modules.

---

Features Implemented

Current capabilities:

- Collect active TCP and UDP connections
- Identify IPv4 and IPv6 connections
- Capture local IP address and local port
- Capture remote IP address and remote port
- Detect whether a remote address is present
- Classify whether the remote IP is external/public
- Capture connection status
- Correlate network connections with process ID
- Capture process name
- Capture process executable path
- Capture process username
- Capture process creation time
- Add host metadata
- Normalize raw connection data into structured SentinelNode events
- Save normalized events as JSON logs
- Provide sanitized sample telemetry output for GitHub

---

Current Architecture

## Current Architecture

main.py
│
├── collector/
│   └── network_collector.py
│
├── sentinel_formatter/
│   └── network_event_formatter.py
│
├── sentinel_logger/
│   └── json_logger.py
│
└── logs/
    └── network_connections.json

Component Responsibilities

"main.py"

Acts as the project entry point. It starts the collector and saves the final output.

"collector/network_collector.py"

Collects raw network and process telemetry from the endpoint.

"sentinel_formatter/network_event_formatter.py"

Converts raw connection data into SentinelNode's normalized event format.

"logs/network_connections.json"

Stores generated runtime telemetry locally. This folder is ignored by Git to avoid publishing raw endpoint data.

"sample_logs/network_connections_sample.json"

Contains sanitized example telemetry output that can be safely viewed on GitHub.

---

Project Structure

SentinelNode/
├── collector/
│   ├── __init__.py
│   └── network_collector.py
├── config/
├── docs/
│   └── phase1_collector_notes.md
├── sample_logs/
│   └── network_connections_sample.json
├── sentinel_formatter/
│   ├── __init__.py
│   └── network_event_formatter.py
├── sentinel_logger/
│   ├── __init__.py
│   └── json_logger.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
---

Normalized Event Format

Example sanitized output:

{
    "timestamp": "2026-06-27T11:45:30.123456",
    "event_type": "network_connection",
    "agent_name": "SentinelNode",
    "agent_phase": "phase_2_event_normalization",
    "hostname": "demo-endpoint-01",
    "network": {
        "protocol_family": "IPv4",
        "protocol": "TCP",
        "local_address": "192.168.1.10",
        "local_port": 53252,
        "remote_address": "93.184.216.34",
        "remote_port": 443,
        "is_remote_present": true,
        "is_external_remote": true,
        "status": "ESTABLISHED"
    },
    "process": {
        "pid": 3225,
        "name": "chrome",
        "executable_path": "/opt/google/chrome/chrome",
        "username": "demo-user",
        "create_time": "2026-06-27T10:33:29.640000"
    }
}

---

How to Run

Clone the repository:

git clone https://github.com/rawat-is-here/sentinel-node.git
cd sentinel-node

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run SentinelNode:

python main.py

View generated logs:

head -40 logs/network_connections.json

---

Example Runtime Output

[[*] SentinelNode Phase 3 Logging Layer Started
[+] Collected and normalized 12 network connection events
[+] Saved 12 events to logs/network_connections.json
[*] SentinelNode Phase 3 Logging Layer Finished

Note: the runtime message may still mention Phase 1 while the internal event format is being upgraded during Phase 2.

---

Security Learning Value

This project helps build practical understanding of:

- Network sockets
- TCP and UDP
- IPv4 and IPv6
- Local and remote addressing
- Process-to-network correlation
- Endpoint telemetry collection
- Public vs private IP classification
- Structured JSON logging
- Event normalization
- SIEM-style event design
- Defensive security project architecture

---

Current Limitations

SentinelNode is still in an early learning phase.

Current limitations:

- No threat intelligence enrichment yet
- No detection rules yet
- No risk scoring yet
- No alerting yet
- No baseline comparison yet
- No dashboard yet
- No database storage yet
- No continuous monitoring loop yet
- No SIEM integration yet

---

Planned Roadmap

Phase 1 — Network Collector

Collect network connections and process context.

Status: Completed.

Phase 2 — Event Normalization

Separate raw collection from event formatting and produce a cleaner normalized event schema.

Status: In progress.

Phase 3 — Logging Layer

Move JSON saving into a dedicated logging module.

Phase 4 — Filtering and Analysis

Separate internal, external, listening, and established connections for analyst-friendly review.

Phase 5 — Detection Rules

Add simple detection rules for suspicious process and network behavior.

Phase 6 — Threat Intelligence

Integrate a threat intelligence provider such as AbuseIPDB.

Phase 7 — Risk Scoring

Assign severity scores based on process, network, and threat intelligence indicators.

Phase 8 — Baseline Engine

Compare current endpoint behavior against previously observed normal behavior.

Phase 9 — Dashboard

Build a simple dashboard to view events and alerts.

Move JSON saving into a dedicated logging module.

Status: Completed.

---

Disclaimer

SentinelNode is a defensive security learning project.

It is not malware, spyware, or an offensive security tool.

It is designed to help understand endpoint telemetry collection, event normalization, and detection engineering at a beginner-friendly level.

Runtime logs may contain local system information, so raw logs are intentionally ignored by Git. Only sanitized sample logs should be committed publicly.
