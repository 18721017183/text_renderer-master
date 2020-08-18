import random

'''读取字典值，存入列表中'''
str = []
with open('../data/chars/char.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        str.append(line)

"""根据字典列表，生成10000字的随机序列。用于图片生成使用"""
str_num = len(str)
with open('../data/corpus/choose_chars.txt','w') as f:
    for i in range(10000):
        idx = random.randint(0,str_num-1)   #头尾都包含，防止越界
        f.write(str[idx])
        if i % 100 == 0 and i != 0:
            f.write('\n')

