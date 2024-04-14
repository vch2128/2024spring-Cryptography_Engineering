import hashlib
import time

def solve_hash(pwds,h,fl):
    start = time.time()
    hash_obj = hashlib.sha1()
    cnt = 0
    for pwd in pwds:
        hash_obj.update(pwd.encode())
        hash_pwd = hash_obj.hexdigest()
        cnt += 1
        if h == hash_pwd:
            break
        hash_obj = hashlib.sha1()
    end = time.time()   
    if fl == True:
        print("Hash:",h)
        print("Password:",pwd)
        print("Took",cnt,"attempts to crack input hash. Time Taken: ",format(end-start),"\n") 
    else:           
        return pwd

def solve_saltedhash(pwds,h,salt):
    start = time.time()
    hash_obj = hashlib.sha1()
    cnt = 0
    for pwd in pwds:
        salted_pwd = salt+pwd
        hash_obj.update(salted_pwd.encode())
        hash_pwd = hash_obj.hexdigest()
        cnt += 1
        if h == hash_pwd:
            break
        hash_obj = hashlib.sha1()
    end = time.time()   
    print("Hash:",h)
    print("Password:",salted_pwd)
    print("Took",cnt,"attempts to crack input hash. Time Taken: ",format(end-start),"\n") 
    
def solve_combinedhash(pwds,h):
    start = time.time()
    hash_obj = hashlib.sha1()
    cnt = 0
    for pwd1 in pwds:
        for pwd2 in pwds:
            new_pwd = pwd1+" "+pwd2
            hash_obj.update(new_pwd.encode())
            hash_pwd = hash_obj.hexdigest()
            cnt += 1
            if h == hash_pwd:
                break
            hash_obj = hashlib.sha1()
    end = time.time()   
    print("Hash:",h)
    print("Password:",new_pwd)
    print("Took",cnt,"attempts to crack input hash. Time Taken: ",format(end-start),"\n") 


h1 = "ef0ebbb77298e1fbd81f756a4efc35b977c93dae"
h2 = "0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2"
salt = "dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06"
h3 = "9d6b628c1f81b4795c0266c0f12123c1e09a7ad3"
h4 = "44ac8049dd677cb5bc0ee2aac622a0f42838b34d"

file_path = 'password.txt'
with open(file_path,'r') as file:
    pwds = [line.strip() for line in file]

print("(a)")
solve_hash(pwds,h1,True)
print("(b)")
solve_hash(pwds,h2,True)
print("(c)")
salt_str = solve_hash(pwds,salt,False)
solve_saltedhash(pwds,h3,salt_str)
# print("(d)")
# solve_combinedhash(pwds,h4)