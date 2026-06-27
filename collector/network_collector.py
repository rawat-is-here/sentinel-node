import json
import socket
import platform
import ipaddress
import psutil
from sentinel_formatter.network_event_formatter import format_network_event
from datetime import datetime
from pathlib import Path


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "network_connections.json"


def get_protocol_family(family):
    if family == socket.AF_INET:
        return "IPv4"
    elif family == socket.AF_INET6:
        return "IPv6"
    else:
        return str(family)


def get_socket_type(socket_type):
    if socket_type == socket.SOCK_STREAM:
        return "TCP"
    elif socket_type == socket.SOCK_DGRAM:
        return "UDP"
    else:
        return str(socket_type)


def is_external_ip(ip_address):
    if ip_address is None:
        return False

    try:
        ip = ipaddress.ip_address(ip_address)

        if ip.is_private:
            return False

        if ip.is_loopback:
            return False

        if ip.is_multicast:
            return False

        if ip.is_link_local:
            return False

        if ip.is_reserved:
            return False

        return True

    except ValueError:
        return False


def collect_network_connections():
    connections = []
    hostname = platform.node()

    for conn in psutil.net_connections(kind="inet"):
        connection_data = {
            "protocol_family": get_protocol_family(conn.family),
            "protocol": get_socket_type(conn.type),
            "local_address": None,
            "local_port": None,
            "remote_address": None,
            "remote_port": None,
            "is_remote_present": False,
            "is_external_remote": False,
            "status": conn.status,
            "pid": conn.pid,
            "process_name": None,
            "process_exe": None,
            "process_username": None,
            "process_create_time": None,
        }

        if conn.laddr:
            connection_data["local_address"] = conn.laddr.ip
            connection_data["local_port"] = conn.laddr.port

        if conn.raddr:
            connection_data["remote_address"] = conn.raddr.ip
            connection_data["remote_port"] = conn.raddr.port
            connection_data["is_remote_present"] = True
            connection_data["is_external_remote"] = is_external_ip(conn.raddr.ip)

        if conn.pid:
            try:
                process = psutil.Process(conn.pid)

                connection_data["process_name"] = process.name()
                connection_data["process_exe"] = process.exe()
                connection_data["process_username"] = process.username()
                connection_data["process_create_time"] = datetime.fromtimestamp(
                    process.create_time()
                ).isoformat()

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                connection_data["process_name"] = "unknown"
                connection_data["process_exe"] = "unknown"
                connection_data["process_username"] = "unknown"
                connection_data["process_create_time"] = "unknown"

        # Moved outside the try/except block so it runs for ALL successful connections
        formatted_event = format_network_event(connection_data, hostname)
        connections.append(formatted_event)

    return connections


def save_connections_to_json(connections):
    LOG_DIR.mkdir(exist_ok=True)

    with open(LOG_FILE, "w") as file:
        json.dump(connections, file, indent=4)
