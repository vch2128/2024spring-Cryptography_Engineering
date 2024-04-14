import random
import itertools

def naive(rate_dict):
    for k in range(1000000):
        cards = ['1','2','3','4']
        for i in range(0,len(cards)-1):
            n = random.randint(0,len(cards)-1)
            temp = cards[i]
            cards[i] = cards[n]
            cards[n] = temp
        cs = ''.join(cards)
        rate_dict[cs] += 1
    

def fisher(rate_dict):
    for k in range(1000000):
        cards = ['1','2','3','4']
        for i in range(len(cards)-1,0,-1):
            n = random.randint(0,i)
            temp = cards[i]
            cards[i] = cards[n]
            cards[n] = temp
        cs = ''.join(cards)
        rate_dict[cs] += 1

def printrate(rate_dict):
    for perm,rate in rate_dict.items():
        print(perm,":",rate)

permutations = itertools.permutations('1234')
permutations2 = itertools.permutations('1234')

rate1 = [0]*24
rate_dict1 = { ''.join(perm): rate1[i] for i,perm in enumerate(permutations) }
rate2 = [0]*24
rate_dict2 = { ''.join(perm): rate2[i] for i,perm in enumerate(permutations2) }
naive(rate_dict1)
fisher(rate_dict2)

print("Naive algorithm:")
printrate(rate_dict1)
print("")
print("Fisher–Yates shuffle:")
printrate(rate_dict2)