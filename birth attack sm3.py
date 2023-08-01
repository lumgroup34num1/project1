import random
import time
from gmssl import sm3, func

#攻击成功率1/2
def Random(n):
    LIST = []
    while len(LIST) < 2**(n/2):
        i = random.randint(0, 2**32-1)
        if i not in LIST:
            LIST.append(i)
    return LIST

def brithAttack(n):
    global list1
    mydist={}
    LIST=Random(n)
    for i in LIST:
        str = i.to_bytes(32 ,"big")
        result = sm3.sm3_hash(func.bytes_to_list(str))[:int(n / 4)]#结果前8bit
        if result not in mydist.values():
            mydist[i]=result
        else :
            list1.append((list(mydist.keys())[list(mydist.values()).index(result)],i))
            return True
    return False


sum1=0
sum2=0
list1=[]
start=time.time()
for i in range(1000):
    if brithAttack(int(8)):
        sum1+=1
end = time.time()
print('前8比特成功率:',sum1/10,'%','耗时：',(end-start)/1000)
start=time.time()
for i in range(100):
    if brithAttack(int(16)):
        sum2+=1
end = time.time()
print('前16比特成功率:',sum2,'%','耗时：',(end-start)/100)