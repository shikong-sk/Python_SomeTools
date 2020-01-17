# import hashlib
# x = 0
# m = hashlib.md5()
# while True:
#     print(x)
#     s = str(x)
#     m.update(s.encode('utf-8'))
#     if m.hexdigest()[0:5] == '94f6d':
#         break
#     else:
#         x += 1
# print(s)
from hashlib import md5  
from string import ascii_letters,digits  
from itertools import permutations  
from time import time  
all_letters=ascii_letters+digits+'.,;'  
def decrypt_md5(md5_value):  
    # if len(md5_value)!=32:  
    #     print('error')  
    #     return  
    md5_value=md5_value.lower()  
    for k in range(5,10):  
        for item in permutations(all_letters,k):  
            item=''.join(item)  
            # print('.',end='')  
            if md5(item.encode()).hexdigest()[0:len(md5_value)]==md5_value:  
                return item  
md5_value = 'b07ef'  
start=time()  
result=decrypt_md5(md5_value)
if result:  
    print('\n Success: '+md5_value+'==>'+result)  
print('Time used:',time()-start)  