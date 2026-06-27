from datetime import datetime


AGENT_NAME = "SentinelNode"
AGENT_PHASE = "phase_2_event_normalization"


def format_network_event(raw_connection, hostname):
    """
    Convert raw network connection data into SentinelNode's standard event format.
    """

    return {
        "timestamp": datetime.now().isoformat(),
        "event_type": "network_connection",
        "agent_name": AGENT_NAME,
        "agent_phase": AGENT_PHASE,
        "hostname": hostname,

        "network": {
            "protocol_family": raw_connection["protocol_family"],
            "protocol": raw_connection["protocol"],
            "local_address": raw_connection["local_address"],
            "local_port": raw_connection["local_port"],
            "remote_address": raw_connection["remote_address"],
            "remote_port": raw_connection["remote_port"],
            "is_remote_present": raw_connection["is_remote_present"],
            "is_external_remote": raw_connection["is_external_remote"],
            "status": raw_connection["status"]
        },

        "process": {
            "pid": raw_connection["pid"],
            "name": raw_connection["process_name"],
            "executable_path": raw_connection["process_exe"],
            "username": raw_connection["process_username"],
            "create_time": raw_connection["process_create_time"]
        }
    }
