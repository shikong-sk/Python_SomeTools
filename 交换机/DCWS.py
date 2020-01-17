import serial
# import chardet

# ser = serial.Serial('com3',9600,timeout=0.5)

ser = serial.Serial('com3', 9600, timeout=0.5)

try:
    ser.open()
# except Exception as error:
#     ser.close()
#     ser.open()
#     pass
except:
    pass

commands = [
    'end',
    'en',
    'conf',
    'ip dh pool pool1',
    'network 172.16.10.0 255.255.255.0',
    'default-router 172.16.10.1',
    'dns-server 8.8.8.8',
    'option 43 hex 0104C0A864FE',
    'ex',
    'wireless',
    'enable',
    'no auto-ip-assign',
    'static-ip 192.168.200.254',
    'ap profile 1',
    'hwtype 59',
    'ex',
    'network 1',
    'ssid dcn2015',
    'security mode wpa-personal',
    'wpa key gsdcn2015',
    'vl 10',
    'ex',
    'ap profile 1',
    'radio 1',
    'vap 0',
    'network 1',
    'ex',
    'ex',
    'ex',
    'network 2',
    'ssid dcntest',
    'security mode none',
    'hide-ssid',
    'ex',
    'ap profile 1',
    'radio 1',
    'vap 1',
    'network 2',
    'ex', 'ex', 'ex',
    'network 2',
    'max-clients 20',
    'client-qos bandwidth-limit up 1024',
    'client-qos bandwidth-limit down 2048',
    'ex',
    'ap profile 1',
    'radio 1',
    'schedule-mode preferred',
    'ex', 'ex',
    'wireless ap anti-flood interval 10',
    'wireless ap anti-flood max-conn-count 5',
    'wireless ap anti-flood agetime 120',
    'ex',
    'username dcn2015 privilege 15 password 0 dcn2015',
    'end'

]

# x = 0
# ser.write(bytes(command[x] + '\n', encoding='utf-8'))
# x += 1
# res = ser.readline()

for command in commands:
    ser.write(bytes(command + '\n', encoding='utf-8'))
    # res = ser.readlines()
    # for text in res:
    #     print(text.decode())
    res = ser.readline()
    print(res.decode())

