from scapy.all import sniff
from scapy.layers.inet import IP
from datetime import datetime
def packet_callback(packet):
    if packet.haslayer(IP):
        protocols = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        proto = protocols.get(packet[IP].proto, "Other")

        print("=" * 60)
        print("Time           :", datetime.now().strftime("%H:%M:%S"))
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", proto)
        print("Packet Length  :", len(packet))

print("Starting Network Sniffer...")
print("Press Ctrl+C to stop.\n")

sniff(prn=packet_callback, store=False)