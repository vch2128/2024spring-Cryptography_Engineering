import random

def xor(a,b):
    if a==b:
        return 0
    return 1

random_lst = [random.randint(0,1) for _ in range(1024*1024*8)]
for i in range(len(random_lst)-1):
    random_lst[i] = xor(random_lst[i],random_lst[i+1])
byte_lst = [random_lst[i:i+8] for i in range(0,len(random_lst),8)]

with open("notrand.bin","ab") as file:
    for byte in byte_lst:
        byte_data = bytes([int(''.join(map(str, byte)), 2)])
        file.write(byte_data)
