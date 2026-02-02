import socket
import threading
import sys
import os
import time

if len(sys.argv) < 3:
    print("Uso: python client.py <IP_SERVIDOR> <usuario>")
    sys.exit(1)

SERVER_IP = sys.argv[1]
USERNAME = sys.argv[2]
PORT = 8443

SALA = "Desconocida"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    banner = r"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |    _______   | || |    ______    | |
| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |   /  ___  |  | || |  .' ___  |   | |
| | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__) |   | || |  |   \/   |  | || |  |  (__ \_|  | || | / .'   \_|   | |
| |     | |      | || |   |  _|  _   | || |   |  __ /    | || |  | |\  /| |  | || |   '.___`-.   | || | | |    ____  | |
| |    _| |_     | || |  _| |___/ |  | || |  _| |  \ \_  | || | _| |_\/_| |_ | || |  |`\____) |  | || | \ `.___]  _| | |
| |   |_____|    | || | |_________|  | || | |____| |___| | || ||_____||_____|| || |  |_______.'  | || |  `._____.'   | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                                                                    "Termsg with no cert" by nestore
"""
    print(banner)
    print(f"Nombre de la sala: {SALA}")
    print("-" * 80)

def redraw():
    clear_screen()
    print_banner()
    print(f"[{USERNAME}]: ", end="", flush=True)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))

# enviar username
sock.send((USERNAME + "\n").encode())

redraw()

def receive_thread():
    global SALA
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                print("\n[-] Desconectado del servidor")
                break

            msg = data.decode().strip()

            if msg.startswith("[SALA]:"):
                SALA = msg.split(":", 1)[1].strip()
                redraw()
                continue

            print("\n" + msg)
            print(f"[{USERNAME}]: ", end="", flush=True)

        except:
            break

def input_thread():
    while True:
        try:
            msg = input()
            if msg == "/quit":
                sock.send(b"/quit\n")
                break
            sock.send((msg + "\n").encode())
            print(f"[{USERNAME}]: ", end="", flush=True)
        except:
            break

threading.Thread(target=receive_thread, daemon=True).start()
threading.Thread(target=input_thread, daemon=True).start()

while True:
    time.sleep(0.1)
