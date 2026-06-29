SentinelNode — Endpoint Telemetry & Threat Detection Agent

SentinelNode is a defensive cybersecurity learning project that simulates the early foundation of a lightweight Endpoint Detection and Response system.

The project collects endpoint network telemetry, enriches it with process context, converts it into a normalized event format, saves it through a dedicated logging layer, and analyzes connection behavior to produce analyst-friendly summaries.

This project is being built step by step to understand how endpoint telemetry, event normalization, logging, connection analysis, detection engineering, threat intelligence enrichment, baselining, and SIEM-style workflows work in real security environments.

---

Current Phase

Phase 4 — Connection Analysis Layer

The current version collects active network connections from the local machine, enriches them with process context, normalizes the collected data into structured SentinelNode events, saves the events as JSON logs, and generates a connection analysis summary.

The analyzer helps answer basic SOC-style questions such as:

- How many total network events were collected?
- How many connections are external/public?
- How many connections are internal or local?
- How many sockets are listening?
- How many connections are established?
- Which processes are communicating externally?
- Which remote ports are being used?

This moves SentinelNode beyond raw telemetry collection and into basic connection behavior analysis.

---

Why This Project Exists

Security teams do not investigate network connections in isolation.

A raw connection like this:

192.168.1.10:53252 → 93.184.216.34:443

only tells us that a machine connected to a remote IP address.

For security analysis, we need more context:

- Which process created the connection?
- Where is the executable located?
- Which user owns the process?
- Is the remote IP private or public?
- Is the connection using TCP or UDP?
- Is the connection established, listening, or closed?
- Did the process start recently?
- Which processes are responsible for external communication?
- Which ports are most commonly observed?

SentinelNode is built to collect this type of endpoint telemetry and gradually evolve into a small defensive detection system.

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
- Save normalized events as JSON logs through a dedicated logging layer
- Analyze collected events and generate a connection summary
- Count external and internal/local connections
- Count listening and established connections
- Summarize processes with external connections
- Summarize observed remote ports
- Provide sanitized sample telemetry output for GitHub

---

Current Architecture

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
├── sentinel_analyzer/
│   └── connection_analyzer.py
│
└── logs/
    └── network_connections.json

Component Responsibilities

"main.py"

Acts as the project entry point and orchestrates collection, formatting, logging, and analysis.

"collector/network_collector.py"

Collects raw network and process telemetry from the endpoint.

"sentinel_formatter/network_event_formatter.py"

Converts raw connection data into SentinelNode's normalized event format.

"sentinel_logger/json_logger.py"

Saves normalized SentinelNode events to JSON log files.

"sentinel_analyzer/connection_analyzer.py"

Analyzes normalized network events and produces an analyst-friendly connection summary.

"logs/network_connections.json"

Stores generated runtime telemetry locally. This folder is ignored by Git to avoid publishing raw endpoint data.

"sample_logs/network_connections_sample.json"

Contains sanitized example telemetry output that can be safely viewed on GitHub.

---

Project Structure

SentinelNode/
├── collector/
│   ├── init.py
│   └── network_collector.py
├── config/
├── docs/
│   └── phase1_collector_notes.md
├── sample_logs/
│   └── network_connections_sample.json
├── sentinel_analyzer/
│   ├── init.py
│   └── connection_analyzer.py
├── sentinel_formatter/
│   ├── init.py
│   └── network_event_formatter.py
├── sentinel_logger/
│   ├── init.py
│   └── json_logger.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

---

Normalized Event Format

Example sanitized event:

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
        "name": "firefox-esr",
        "executable_path": "/usr/lib/firefox-esr/firefox-esr",
        "username": "demo-user",
        "create_time": "2026-06-27T10:33:29.640000"
    }
}

---

Example Analysis Output

Example runtime summary:

[*] SentinelNode Phase 4 Connection Analysis Started
[+] Collected and normalized 74 network connection events
[+] Saved 74 events to logs/network_connections.json

[*] SentinelNode Connection Analysis Summary
[+] Total events: 74
[+] External connections: 43
[+] Internal/local connections: 31
[+] Listening connections: 3
[+] Established connections: 26

[*] Processes with external connections:
    - unknown: 17
    - firefox-esr: 26

[*] Remote ports observed:
    - Port 443: 39
    - Port 67: 1
    - Port 80: 4

[*] SentinelNode Phase 4 Connection Analysis Finished

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

Useful Commands

Run syntax checks:

python -m py_compile main.py collector/network_collector.py sentinel_formatter/network_event_formatter.py sentinel_logger/json_logger.py sentinel_analyzer/connection_analyzer.py

View the first part of the generated JSON log:

head -60 logs/network_connections.json

Check external connections in the generated log:

grep '"is_external_remote": true' logs/network_connections.json

Check process names in the generated log:

grep '"name"' logs/network_connections.json

---

Security Learning Value

This project helps build practical understanding of:

- Network sockets
- TCP and UDP
- IPv4 and IPv6
- Local and remote addressing
- Connection states
- Process-to-network correlation
- Endpoint telemetry collection
- Public vs private IP classification
- Structured JSON logging
- Event normalization
- Dedicated logging architecture
- Basic connection analysis
- Analyst-style network summaries
- SIEM-style event design
- Defensive security project architecture

---

Current Limitations

SentinelNode is still in an early learning phase.

Current limitations:

- No detection rules yet
- No alert generation yet
- No risk scoring yet
- No threat intelligence enrichment yet
- No baseline comparison yet
- No dashboard yet
- No database storage yet
- No continuous monitoring loop yet
- No SIEM integration yet
- No configuration file support yet
- No unit tests yet

---

Planned Roadmap

Phase 1 — Network Collector

Collect network connections and process context.Status: Completed.

Phase 2 — Event Normalization

Separate raw collection from event formatting and produce a cleaner normalized event schema.

Status: Completed.

Phase 3 — Logging Layer

Move JSON saving into a dedicated logging module.

Status: Completed.

Phase 4 — Connection Analysis Layer

Analyze normalized events and summarize external connections, internal/local connections, listening sockets, established connections, process-level external communication, and observed remote ports.

Status: Completed.

Phase 5 — Basic Detection Rules

Add simple rule-based detections for suspicious process and network behavior.

Planned examples:

- External connection from unknown process
- External connection on unusual remote port
- Listening socket from suspicious process
- Process running from unusual path
- High number of external connections from one process

Phase 6 — Alert Generation

Convert detection results into structured alert objects.

Phase 7 — Risk Scoring

Assign severity scores based on network, process, and detection indicators.

Phase 8 — Threat Intelligence

Integrate a threat intelligence provider such as AbuseIPDB.

Phase 9 — Baseline Engine

Compare current endpoint behavior against previously observed normal behavior.

Phase 10 — Dashboard

Build a simple dashboard to view events, summaries, and alerts.

---

Example Resume Description

SentinelNode is a modular defensive security project that collects endpoint network telemetry, correlates it with process metadata, normalizes it into structured JSON events, logs it through a dedicated logging layer, and analyzes connection behavior to summarize external communication, listening sockets, connection states, process-level activity, and observed remote ports.

---

Disclaimer

SentinelNode is a defensive security learning project.

It is not malware, spyware, or an offensive security tool.

It is designed to help understand endpoint telemetry collection, event normalization, logging architecture, connection analysis, and detection engineering at a beginner-friendly level.

Runtime logs may contain local system information, so raw logs are intentionally ignored by Git. Only sanitized sample logs should be committed publicly.
