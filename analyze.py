import platform

import psutil

# import os
# import subprocess


def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "CPU Count": psutil.cpu_count(),
        "CPU Usage": psutil.cpu_percent(interval=1),
        "Memory": {
            "Total": psutil.virtual_memory().total,
            "Available": psutil.virtual_memory().available,
            "Used": psutil.virtual_memory().used,
            "Percentage": psutil.virtual_memory().percent,
        },
        "Disk": {
            "Total": psutil.disk_usage("/").total,
            "Used": psutil.disk_usage("/").used,
            "Free": psutil.disk_usage("/").free,
            "Percentage": psutil.disk_usage("/").percent,
        },
        "Uptime": psutil.boot_time(),
        "Running Processes": [p.info for p in psutil.process_iter(["pid", "name"])],
        "Hostname": platform.node(),
        "Network Interfaces": get_network_info(),
    }
    return system_info


def get_network_info():
    interfaces = psutil.net_if_addrs()
    return {
        interface: [addr.address for addr in addresses]
        for interface, addresses in interfaces.items()
    }


if __name__ == "__main__":
    info = get_system_info()
    print(info)
