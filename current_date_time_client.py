import socket

with socket.socket() as s:
    s.connect(('127.0.0.1', 12345))
    s.send(b"get time")
    print("Current server time:", s.recv(1024).decode())

input("\nPress Enter to exit...")
