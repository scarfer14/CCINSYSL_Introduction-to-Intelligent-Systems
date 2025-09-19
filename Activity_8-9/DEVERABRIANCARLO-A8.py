from scapy.all import sniff
from collections import defaultdict
import time
import csv
import os

# Threshold for suspicious activity
THRESHOLD = 5

# Packet counts per source
packet_counts = defaultdict(int)

# Log file (CSV)
LOG_FILE = "ids_alerts.csv"

def log_alert(src_ip, count, message):
    """Write alerts to both console and CSV file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")  # Print to console
    
    # Append to CSV
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, src_ip, count, message])

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        packet_counts[src_ip] += 1
        print(f"Packet from: {src_ip} (count: {packet_counts[src_ip]})")

        # Check threshold
        if packet_counts[src_ip] > THRESHOLD:
            log_alert(src_ip, packet_counts[src_ip],
                      f"Suspicious activity detected from {src_ip}. "
                      f"Packets sent: {packet_counts[src_ip]}")

if __name__ == "__main__":
    print("Starting live packet capture... (press Ctrl+C to stop)")

    # Create/clear the CSV log file with headers
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Source IP", "Packet Count", "Message"])

    sniff(prn=packet_callback, count=50)  # capture 50 packets
    print(f"\nAlerts logged to {LOG_FILE}")
