import socket

HEADER_SIZE = 10
IP = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((IP, PORT))

while True:
    send_msg = input()
    send_msg = f"{len(send_msg):<{HEADER_SIZE}}{send_msg}"
    server_socket.send(bytes(send_msg, "utf-8"))

    full_recv_msg = ""
    new_msg = True
    msg_len = 0

    while True:
        recv_msg = server_socket.recv(16).decode("utf-8")
        full_recv_msg += recv_msg

        if new_msg:
            msg_len = int(recv_msg[:HEADER_SIZE])
            new_msg = False

        if len(full_recv_msg) == msg_len + HEADER_SIZE:
            break

    print(f"Server: {full_recv_msg[HEADER_SIZE:]}")
