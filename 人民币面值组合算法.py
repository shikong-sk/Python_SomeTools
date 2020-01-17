dp = []
maxn = 10000 + 1
num = [5,10,20,50,100]
for i in range(maxn):
	dp.append(1)
for i in range(5):
	for j in range(num[i],maxn):
		dp[j] += dp[j - num[i]]
print('面值 1',end='')
for x in num:print(',',x,end='')
print('的人民币组成',maxn - 1,'元\n有' ,dp[maxn - 1] , '种解法')