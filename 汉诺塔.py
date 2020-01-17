import sys
def 汉诺塔(x,a,b,c):
	if x==1:
		print(a,'-->',c)
	else:
		汉诺塔(x-1,a,c,b)
		汉诺塔(1,a,b,c)
		汉诺塔(x-1,b,a,c)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('请输入移动的盘数：')
		盘数 = int(input())
	else:
		盘数 = int(sys.argv[1])
	汉诺塔(盘数,'A','B','C')
	