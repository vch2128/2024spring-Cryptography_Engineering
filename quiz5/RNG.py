from random import SystemRandom
rng = SystemRandom()

random_lst = [rng.randrange(2) for i in range(1048576*8)]
byte_lst = [random_lst[i:i+8] for i in range(0,len(random_lst),8)]

with open("random.bin","ab") as file:
    for byte in byte_lst:
        byte_data = bytes([int(''.join(map(str, byte)), 2)])
        file.write(byte_data)
        
