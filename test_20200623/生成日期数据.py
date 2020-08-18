import time
import random

a1=(2019,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2022,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）

start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳

end_chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chars_num = len(end_chars)
str = ''
#随机生成10个日期字符串
for i in range(10):
    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("%Y/%m/%d",date_touple)  #将时间元组转成格式化字符串（1976/05/21）
    k = random.randint(0,chars_num)
    str = str + '-'.join([date,end_chars[k]]) + '\n'
    print('-'.join([date,end_chars[k]]))

with open('../data/corpus/choose_chars.txt','w') as f:
    f.write(str)
print(str)