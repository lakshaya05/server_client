import socket
24
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
def main():
 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client.connect(ADDR)
 print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
 connected = True
 while connected:
 msg = input("> ")
 client.send(msg.encode(FORMAT))
 if msg == DISCONNECT_MSG:
 connected = False
 else:
 msg = client.recv(SIZE).decode(FORMAT)
 print(f"[SERVER] {msg}")
if _name_ == "_main_":
 main()
6.5 Server.py
import socket
import threading
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
def handle_client(conn, addr):
 print(f"[NEW CONNECTION] {addr} connected.")
 connected = True
 while connected:
 msg = conn.recv(SIZE).decode(FORMAT)
 if msg == DISCONNECT_MSG:
 connected = False
 print(f"[{addr}] {msg}")
 msg = f"Msg received: {msg}"
 conn.send(msg.encode(FORMAT))
 conn.close()
def main():
 print("[STARTING] Server is starting...")
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 server.bind(ADDR)
 server.listen()
 print(f"[LISTENING] Server is listening on {IP}:{PORT}")
 while True:
 conn, addr = server.accept()
 thread = threading.Thread(target=handle_client, args=(conn, addr))
 thread.start()
 print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
if _name_ == "_main_":
 main()
