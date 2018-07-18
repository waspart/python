import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect_ex(("127.0.0.1", 8888))

while True:
    msg = input(">>:").strip()
    # print(msg, len(msg))
    if len(msg) == 0:
        continue

    sk.send(msg.encode('utf-8'))
    ret = str(sk.recv(1024), encoding="utf-8")
    print(ret)
# sk.shutdown(socket.SHUT_RDWR)
sk.close()