# live_ids.py
from scapy.all import sniff
from collections import defaultdict
import time
import os

# Threshold for suspicious activity
THRESHOLD = 5

# Packet counts per source
packet_counts = defaultdict(int)

# Log file
LOG_FILE = "ids_alerts.log"

def log_alert(message):
    """Write alerts to both console and file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    print(entry.strip())  # Print to console
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        packet_counts[src_ip] += 1
        print(f"Packet from: {src_ip} (count: {packet_counts[src_ip]})")

        # Check threshold
        if packet_counts[src_ip] > THRESHOLD:
            log_alert(f"!!! ALERT: Suspicious activity detected from {src_ip}. "
                      f"Packets sent: {packet_counts[src_ip]}")

if __name__ == "__main__":
    print("Starting live packet capture... (press Ctrl+C to stop)")

    # Create/clear the log file at start
    with open(LOG_FILE, "w") as f:
        f.write("=== IDS Log Started ===\n")

    sniff(prn=packet_callback, count=50)  # capture 50 packets
    print(f"\nAlerts logged to {LOG_FILE}")
