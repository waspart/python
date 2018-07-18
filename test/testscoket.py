import socket

ipaddr = '115.159.193.122'
port = 7979
img_url = b'http://imgbdb2.bendibao.com/szbdb/20146/7/2014671270642.jpg'
message = b'Pis_OCR {COMM_INFO {BUSI_CODE 10011} {REGION_ID A} {COUNTY_ID A00} {OFFICE_ID robot} {OPERATOR_ID 44444}  {CHANNEL A2} {OP_MODE SUBMIT}} { {PIC_URL {' + img_url + b'}} }'
# img_url = 'http://imgbdb2.bendibao.com/szbdb/20146/7/2014671270642.jpg'

print(message)

tcp_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = (ipaddr, port)
tcp_fd.connect(server_addr)

tcp_fd.send(message)

print(tcp_fd.recv(1024))
print(tcp_fd.getpeername())
print(tcp_fd.getsockname())

tcp_fd.close()

