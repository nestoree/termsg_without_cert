from scapy.all import sniff, TCP, Raw, IP
import datetime

user_port = input("[+] Introduce el puerto: ")

CHAT_PORT = user_port 

def packet_handler(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        tcp = packet[TCP]

        # Solo tráfico del puerto del chat
        if tcp.sport == CHAT_PORT or tcp.dport == CHAT_PORT:
            payload = packet[Raw].load

            try:
                text = payload.decode("utf-8", errors="ignore").strip()
                if text:
                    ts = datetime.datetime.now().strftime("%H:%M:%S")
                    src = packet[IP].src
                    dst = packet[IP].dst
                    print(f"[{ts}] {src} -> {dst}: {text}")
            except:
                pass


print("[*] Esnifando tráfico del chat...")
print(f"[*] Puerto TCP: {CHAT_PORT}")

sniff(filter=f"tcp port {CHAT_PORT}", prn=packet_handler, store=False)
