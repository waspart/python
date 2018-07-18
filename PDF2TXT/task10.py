# 调用现有OCR接口

import socket
import time

t0 = time.clock()

host = '115.159.193.122'
port = 7979
content = 'http://imgbdb2.bendibao.com/szbdb/20146/7/2014671270642.jpg'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('s 的类型：', type(s))
connres = s.connect_ex((host, port))
print('连接状态：', connres)
# s.bind((host, port))

# msg = r'Pis_OCR {COMM_INFO {BUSI_CODE 10011} {REGION_ID A} {COUNTY_ID A00} {OFFICE_ID robot} {OPERATOR_ID 44444} {
# CHANNEL A2} {OP_MODE SUBMIT}} { {PIC_URL {' + content + r'}} }'
msg = r'Pis_OCR {COMM_INFO {BUSI_CODE 10011} {REGION_ID A} {COUNTY_ID A00} {OFFICE_ID robot} {OPERATOR_ID 44444} {' \
      r'CHANNEL A2} {OP_MODE SUBMIT}} { {PIC_URL {http://imgbdb2.bendibao.com/szbdb/20146/7/2014671270642.jpg}} } '
print('请求串：', bytes(msg.replace(' ', ''), encoding='utf-8'))
print(len(msg.replace(' ', '')))
s.send(bytes(msg, encoding='utf-8'))
#s.sendall(bytes(msg))
# time.sleep(10)
# total_rmsg = []
# while True:
#     rmsg = s.recv(1024)
#     print(rmsg is None)
#     print(isinstance(rmsg, bytes))
#     if not rmsg:
#         break
#     total_rmsg.append(rmsg)
rmsg = s.recv(10240)

print('连接耗时：', time.clock() - t0)
print('返回信息类型：', type(rmsg))
print('返回信息：', rmsg)

s.close()
