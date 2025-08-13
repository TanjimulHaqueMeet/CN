import socket, datetime, threading

def handle_client(c, a):
    print(f"Connected: {a}")
    try:
        req = c.recv(1024).decode().lower()
        msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") if req == "get time" else "Invalid request"
        c.send(msg.encode())
    finally:
        c.close()
        print(f"Closed: {a}")

def start_server(host='127.0.0.1', port=12345):
    with socket.socket() as s:
        s.bind((host, port))
        s.listen()
        print(f"Server on {host}:{port}")
        while True:
            threading.Thread(target=handle_client, args=s.accept()).start()

if __name__ == "__main__":
    start_server()
