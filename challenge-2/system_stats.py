#!/usr/bin/env uv run

import sys
import psutil
import argparse

PADDING = 20
LONG_PADDING = 30
EXTRA_WIDE_PADDING = 50
SHORT_PADDING = 7

def as_mb(bytes: int) -> str:
    return f"{bytes / (1024**2):.0f}"

def as_gb(bytes: int) -> str:
    return f"{bytes / (1024**3):.0f}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="simple Python script that can be used to get system information.")
    parser.add_argument("-d", "--disk", action="store_true", help="check disk stats")
    parser.add_argument("-c", "--cpu", action="store_true", help="check cpu stats")
    parser.add_argument("-p", "--ports", action="store_true", help="check listen ports")
    parser.add_argument("-r", "--ram", action="store_true", help="check ram stats")
    parser.add_argument("-o", "--overview", action="store_true", help="top 10 process with most CPU usage")
    args = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    res = ""
    if args.disk:
        res += "# Disk Stats\n"
        res += "Device".ljust(PADDING, " ")
        res += "Mountpoint".ljust(LONG_PADDING, " ")
        res += "Total (MB)".ljust(PADDING, " ")
        res += "Used (MB)".ljust(PADDING, " ")
        res += "Free (MB)".ljust(PADDING, " ")
        res += "Used (%)".ljust(PADDING, " ")
        res += "\n"
        for partition in psutil.disk_partitions():
            usage = psutil.disk_usage(partition.mountpoint)
            res += partition.device.ljust(PADDING, " ")
            res += partition.mountpoint.ljust(LONG_PADDING, " ")
            res += as_mb(usage.total).ljust(PADDING, " ")
            res += as_mb(usage.used).ljust(PADDING, " ")
            res += as_mb(usage.free).ljust(PADDING, " ")
            res += str(usage.percent).ljust(PADDING, " ")
            res += "\n"
        res += "\n"

    if args.cpu:
        res += "# CPU Stats\n"
        res += f"Cores: {psutil.cpu_count()}\n"
        res += f"Usage: {psutil.cpu_percent(interval=0.4)} %\n"
        res += f"Frequency: {psutil.cpu_freq().current}\n"
        res += "\n"

    if args.ram:
        res += "# RAM Stats\n"
        ram = psutil.virtual_memory()
        res += f"Total: {as_gb(ram.total)} GB\n"
        res += f"Available: {as_gb(ram.available)} GB\n"
        res += f"Used: {as_gb(ram.used)} GB\n"
        res += f"Percent: {ram.percent} %\n"
        res += "\n"

    if args.ports:
        res += "# Port Stats\n"
        res += "Listening on: "
        ports = set()
        for proc in psutil.process_iter():
            try:
                for x in proc.net_connections():
                    if x.status == psutil.CONN_LISTEN:
                        ports.add(str(x.laddr.port))
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                # Some processes require additional permissions the user doesn't have, so we skip them
                continue
        res += f"{', '.join(sorted(list(ports), key=int))}\n\n"

    if args.overview:
        res += "# Top 10 CPU Processes\n"
        res += "PID".ljust(SHORT_PADDING) 
        res += "Name".ljust(EXTRA_WIDE_PADDING)
        res += "CPU (%)".ljust(PADDING)
        res += "\n"
        processes = []
        for idx, proc in enumerate(psutil.process_iter(["pid", "name", "cpu_percent"])):
            try:
                processes.append((proc.info, proc.cpu_percent(interval=0.002)))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Some processes require additional permissions the user doesn't have, so we skip them
                continue
        top_processes = sorted(processes, key=lambda x: x[1], reverse=True)[:10]
        for (p, c) in top_processes:
            res += str(p["pid"]).ljust(SHORT_PADDING)
            res += str(p["name"]).ljust(EXTRA_WIDE_PADDING)
            res += f"{c:.2f}".ljust(PADDING)
            res += "\n"

    print(res.strip())

    