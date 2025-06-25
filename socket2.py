import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.connect(("data.pr4e.org", 80))
    cmd = "GET /intro-short.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n".encode()
    my_socket.send(cmd)

    while True:
        data = my_socket.recv(1024)
        if len(data) < 1:
            break
        print(data.decode())
