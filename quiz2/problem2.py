import hashlib
import time

def hash_md5(file):
    start = time.time()
    hash_obj = hashlib.md5(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

def hash_sha1(file):
    start = time.time()
    hash_obj = hashlib.sha1(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

def hash_sha224(file):
    start = time.time()
    hash_obj = hashlib.sha224(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

def hash_sha256(file):
    start = time.time()
    hash_obj = hashlib.sha256(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

def hash_sha512(file):
    start = time.time()
    hash_obj = hashlib.sha512(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

def hash_sha3_224(file):
    start = time.time()
    hash_obj = hashlib.sha3_224(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

def hash_sha3_256(file):
    start = time.time()
    hash_obj = hashlib.sha3_256(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

def hash_sha3_512(file):
    start = time.time()
    hash_obj = hashlib.sha3_512(file)
    hash_pwd = hash_obj.hexdigest()
    end = time.time()
    return format(end-start)

file_path = 'video.mp4'
with open(file_path,'rb') as f:
    file = f.read()

hash_time = [("MD5",hash_md5(file)), 
             ("SHA1",hash_sha1(file)), 
             ("SHA224",hash_sha224(file)),
             ("SHA256",hash_sha256(file)),
             ("SHA512",hash_sha512(file)),
             ("SHA3-224",hash_sha3_224(file)),
             ("SHA3-256",hash_sha3_256(file)),
             ("SHA3-512",hash_sha3_512(file)) ]
hash_time.sort(key=lambda a:a[1])
# for h, t in hash_time:
#     print(h,":",t)
print("The fastest hash algorithm is",hash_time[0][0])
print("Rank of speed:")
rank = 0
for tup in hash_time:
    print(" Rank",rank+1,hash_time[rank][0])
    rank += 1