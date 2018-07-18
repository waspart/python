import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(("127.0.0.1", 8888))
sk.listen(5)

while True:
    # print("Server waiting....")
    conn, address = sk.accept()

    print(conn)
    print("来自%s的电话" %address[0])

    msg = conn.recv(1024)
    print("client message is : ", msg)

    conn.send(msg.upper())

    conn.close()
sk.close()
