#coding=utf-8
#encoding=utf-8

from multiprocessing.pool import ThreadPool
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as DummyPool
from multiprocessing import cpu_count
import subprocess
import time
import sys

address_D = '192.168.1';
address_Min = 1;
address_MAX = 254 + 1;

def kill():
	# subprocess.call('taskkill -f -im ping.exe',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	# subprocess.call('taskkill -f -im python.exe',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	subprocess.Popen('taskkill -f -im ping.exe',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	subprocess.Popen('taskkill -f -im python.exe',stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def address():
	if len(sys.argv) > 2:
		x = str(sys.argv[2])
	else:
		x = address_D
	return x;

def ping_ip(ip):
	global address_D
	global online
	address_D = address()
	ip = str(address_D) + '.' + str(ip)
	res = subprocess.call('ping -n 1 -w 1 -l 1 %s' % ip,stdout=subprocess.PIPE)
	#res = subprocess.Popen('ping -n 1 -w 1 -l 1 %s' % ip,stdout=subprocess.PIPE)
	# print(ip,res)
	# print(address_D)
	#x = str(res.stdout.read())
	# print(x)
	if res == 0:
	# 	print(ip)
		return ip
	# if '100%' not in x:
	# 	return ip
	# if x.find('100%') == -1:
	# 	return ip

def Thread_pool(num):
	global address_Min
	global address_MAX
	res = []
	sk = []
	p = ThreadPool(num)
	start_time = time.time()
	for x in range(address_Min,address_MAX):
		#p.apply_async(ping_ip, args=(x,))
		res.append(p.apply_async(ping_ip, args=(x,)))
		#res.append(p.apply_async(ping_ip, args=(x,)).get())
		#print(p.apply_async(ping_ip, args=(x,)))
	# for y in res:
	# 	if y.get():
	# 		sk.append(y.get())
	# print(sk)
	#End_Time = time.time()
	# if res:
	# 	print('在线主机：\n',res)
	# else:
	# 	print('无在线主机')
	print('在线主机：')

	for y in res:
		if y.get() != None:
			sk.append(y.get())
			# print(y.get())
			# sk = sk + 1
			#sk = list(filter(None, sk))
	sk = list(filter(None, sk))
	if sk:
		print(sk)
	# if res:
	# 	print(res)
	# else:
	# 	print('无在线主机')
	# End_Time = time.time()
	# p.close()
	# p.join()
	#print('共ping',address_MAX - 1,'台机器\n','耗时：%fs\n' % (End_Time - start_time))
	End_Time = time.time()
	print('共ping',address_MAX - 1,'台机器\n','共计',len(sk),'台在线\n','实际耗时：%fs\n' % (End_Time - start_time))
	p.close()
	p.join()
	kill()

def process_pool(num):
	global address_Min
	global address_MAX
	global address_D
	res = []
	sk = []
	p = ProcessPool(num)
	start_time = time.time()
	for x in range(address_Min,address_MAX):
		res.append(p.apply_async(ping_ip, args=(x,)))
		#res.append(p.apply_async(ping_ip, args=(x,)).get())
		#print(p.apply_async(ping_ip, args=(x,)))
	# for y in res:
	# 	if y.get():
	# 		sk.append(y.get())
	# if sk:
	# 	print('在线主机：\n',sk)
	# else:
	# 	print('无在线主机')
	# End_Time = time.time()
	print('在线主机：')
	for y in res:
		if y.get() != None:
			sk.append(y.get())
			# print(y.get())
			# sk = sk + 1
			#sk = list(filter(None, sk))
	sk = list(filter(None, sk))
	if sk:
		print(sk)
	End_Time = time.time()
	print('共ping',address_MAX - 1,'台机器\n','共计',len(sk),'台在线\n','实际耗时：%fs\n' % (End_Time - start_time))
	p.close()
	p.join()
	kill()

def dummy_pool(num):
	global address_Min
	global address_MAX
	res = []
	sk = []
	p = DummyPool(num)
	start_time = time.time()
	for x in range(address_Min,address_MAX):
		res.append(p.apply_async(ping_ip, args=(x,)))
		#res.append(p.apply_async(ping_ip, args=(x,)).get())
		#print(p.apply_async(ping_ip, args=(x,)))
	# End_Time = time.time()
	# for y in res:
	# 	if y.get():
	# 		sk.append(y.get())
	# if sk:
	# 	print('在线主机：\n',sk)
	# else:
	# 	print('无在线主机')
	print('在线主机：')
	End_Time = time.time()
	for y in res:
		if y.get() != None:
			sk.append(y.get())
			# print(y.get())
			# sk = sk + 1
			#sk = list(filter(None, sk))
	sk = list(filter(None, sk))
	if sk:
		print(sk)
	End_Time = time.time()
	print('共ping',address_MAX - 1,'台机器\n','共计',len(sk),'台在线\n','实际耗时：%fs\n' % (End_Time - start_time))
	p.close()
	p.join()
	kill()

def single_thread():
	global address_Min
	global address_MAX
	start_time = time.time()
	res = []
	sk = []
	for x in range(address_Min,address_MAX):
		res.append(ping_ip(x))
	# w = list(filter(None, w))
	# if w:
	# 	print('在线主机：\n',w)
	# else:
	# 	print('无在线主机')
	# End_Time = time.time()
	print('在线主机：')
	sk = list(filter(None, res))
	if sk:
		print(sk)
	End_Time = time.time()
	print('共ping',address_MAX - 1,'台机器\n','共计',len(sk),'台在线\n','耗时：%fs\n' % (End_Time - start_time))
	kill()

if __name__ == '__main__':
	# print('多种算法ping',address_MAX - 1,'台机器')

	# print('单线程算法：')
	# single_thread()

	# print('多进程算法：')
	# process_pool(cpu_count())

	# print('多线程算法1：')
	# Thread_pool(cpu_count() * 10)

	# print('多线程算法2：')
	# dummy_pool(cpu_count() * 10)
	if len(sys.argv) > 5 or len(sys.argv) < 2:
		print('请输入1~4个参数：算法 网络号[默认192.168.1] 主机号范围(例： 1 254 )[默认1~254]')
		print('算法：')
		print('1 为单线程'.center(15))
		print('2 为多进程'.center(15))
		print('3 为多线程算法-1'.center(20))
		print('4 为多线程算法-2'.center(20))
		exit(1)
	else:
		算法 = int(sys.argv[1])
		# if len(sys.argv) > 2:
		# 	address_D = str(sys.argv[2])
		if len(sys.argv) > 3:
			address_Min = int(sys.argv[3])
		if len(sys.argv) > 4:
			address_MAX = int(sys.argv[4]) + 1
		if address_MAX < address_Min:
			address_Min,address_MAX = address_MAX,address_Min 
		y = int(((address_MAX - address_Min + 1) + 10 ) / 10)
		x = cpu_count() * (y)
		if x > cpu_count() * 8:
			x = cpu_count() * 8
		if 算法 == 1:
			single_thread()
		elif 算法 == 2:
			process_pool(cpu_count())
		elif 算法 == 3:
			#print(x,y)
			Thread_pool(x)
		elif 算法 == 4:
			dummy_pool(x)
		elif 算法 > 4 or 算法 < 1:
			print('\nError：算法选择有误')
			exit(1)
	# for x in sys.argv:
	# 	print(x)