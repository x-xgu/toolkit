import random
import socket

from pyais import encode_dict

server = ('10.233.18.23', 5003)  # AIS 转发地址

mmi = 10000001  # 船舶唯一标识

name = '鲁001'  # 船只名称

course = random.uniform(0.5, 1.0)  # 目标对地航向

speed = 1  # 目标对地航速

# 405866
lon = 119.409277  # 目标经度

# 172051
lat = 25.171061  # 目标经度

msg_decode = {'mmsi': mmi, 'shipname': name, 'type': 1, 'course': course, 'speed': speed, 'lon': lon, 'lat': lat}

msg_encode = encode_dict(msg_decode, talker_id='AIVDM')[0]  # 加密

print(msg_decode)

print(msg_encode)

# 使用 Socket 发送消息
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg_encode.encode(), server)



