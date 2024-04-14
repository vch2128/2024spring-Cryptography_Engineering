
def vowel_diff(str,exp):
    vowels = 'AEIOU'
    vowel_count = 0
    
    for char in str:
        if char in vowels:
            vowel_count += 1
    
    diff = vowel_count - exp
    if diff<0:
        diff=-diff

    return diff

def print_separately(string,x,y):
    ini_str = [[] for _ in range(x)]
    cnt=0
    for i in range(y):
        for j in range(x):
            ini_str[j].append(string[cnt])
            cnt +=1
    # print(ini_str)
    diff_lst = []
    for i in range(x):
        str=''.join(ini_str[i])
        diff=vowel_diff(str, y*0.4)
        print(str,diff)
        diff_lst.append(diff)
    
    print("average difference:",sum(diff_lst)/len(diff_lst),"\n")
    return ini_str

cipher = "UONCSVAIHGEPAAHIGIRLBIECSTECSWPNITETIENOIEEFDOWECXTRSRXSTTARTLODYFSOVNEOECOHENIODAARQNAELAFSGNOPTE"
print_separately(cipher,2,49)
print_separately(cipher,7,14)
strs = print_separately(cipher,14,7)
print_separately(cipher,49,2)

nums = [4,1,5,6,0,3,2]

for i in range(14):
    for num in nums:
        print(strs[i][num],end="")
    print("")
