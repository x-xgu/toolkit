length = 5200  # 电缆总长
location = 3800  # 省南跨湖1线山塘变-1号塔8号本体段  3524 4024 3800
rate = 0.5  # 分辨率
normal_val = 44  # 正常数据
abnormal_val = 200  # 异常数据
dts_val = [normal_val] * (int(location / rate)) \
          + \
          [abnormal_val] \
          + \
          [normal_val] * (int(length / rate) - int(location / rate))
print(dts_val)
