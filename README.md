# SentinelNode — Endpoint Telemetry & Threat Detection Agent

SentinelNode is a beginner-friendly defensive security project that simulates the first layer of a lightweight Endpoint Detection and Response system.

The goal of this project is to collect endpoint network telemetry, enrich it with process context, and gradually build toward detection engineering, threat intelligence enrichment, baseline comparison, and SIEM-ready logging.

This project is being built step by step as a learning-focused cybersecurity portfolio project.

---

## Current Phase

### Phase 1 — Network Connection Collector

The current version collects active network connections from the local machine and stores them as structured JSON logs.

The collector captures:

- Timestamp
- Event type
- Agent name
- Agent phase
- Hostname
- Protocol family: IPv4 or IPv6
- Protocol: TCP or UDP
- Local IP address
- Local port
- Remote IP address
- Remote port
- Whether a remote connection exists
- Whether the remote IP is external/public
- Connection status
- PID
- Process name
- Process executable path
- Process username
- Process creation time

---

## Why This Project Exists

Security teams need endpoint telemetry to understand what is happening on a machine.

A network connection alone is not enough.

For example:

```text
192.168.247.129:52038 → 142.250.4.119:443
