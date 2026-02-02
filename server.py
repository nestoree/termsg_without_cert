import socket
import threading
import sys

if len(sys.argv) < 2:
    print("Uso: python server.py <nombre_de_sala>")
    sys.exit(1)

SALA = sys.argv[1]
HOST = "0.0.0.0"
PORT = 8443

clients = []  # [(conn, username)]
lock = threading.Lock()
running = True

def safe_send(conn, msg):
    try:
        conn.send((msg + "\n").encode())
    except:
        pass

def broadcast(msg, exclude=None):
    with lock:
        for conn, _ in clients:
            if conn != exclude:
                safe_send(conn, msg)

def handle_client(conn, addr):
    username = None
    try:
        username = conn.recv(1024).decode().strip()
        if not username:
            return

        with lock:
            clients.append((conn, username))

        print(f"[+] {username} se ha unido desde {addr[0]}", flush=True)
        safe_send(conn, f"[SALA]: {SALA}")
        broadcast(f"[+] {username} se ha unido", conn)

        while running:
            data = conn.recv(1024)
            if not data:
                break

            msg = data.decode().strip()

            if msg == "/quit":
                break
            elif msg == "/usuarios":
                with lock:
                    users = ", ".join(u for _, u in clients)
                safe_send(conn, f"[Usuarios]: {users}")
            else:
                full_msg = f"[{username}]: {msg}"
                print(full_msg, flush=True)
                broadcast(full_msg, conn)

    finally:
        if username:
            with lock:
                clients[:] = [(c, u) for c, u in clients if c != conn]
            broadcast(f"[-] {username} ha salido")
            print(f"[-] {username} desconectado", flush=True)

        try:
            conn.close()
        except:
            pass

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)

    print(f"🟢 Termsg SIN CIFRADO en {HOST}:{PORT} — Sala: {SALA}", flush=True)

    while running:
        try:
            conn, addr = server.accept()
            threading.Thread(
                target=handle_client, args=(conn, addr), daemon=True
            ).start()
        except KeyboardInterrupt:
            print("\n[!] Servidor detenido")
            break

    server.close()

if __name__ == "__main__":
    main()
