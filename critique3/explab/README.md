## Diffie-Hellman Algorithm 實作

### 介紹
此程式碼展示如何實作 Diffie-Hellman 密鑰交換算法。該算法允許兩個用戶在不安全的通道上生成共享密鑰，而不需要提前交換秘密信息，最後使用生成的共享密鑰進行AES加密和解密。

### 使用的套件
- cryptography：提供加密算法和模式的實現，包括AES和CBC模式
- hashlib：提供SHA-256哈希函數
- random：生成隨機數
- os：生成隨機初始化向量（IV）

### 如何執行
```
pip install -r requirements.txt
python diffie_hellman.py
```
### 執行步驟
1. 定義質數p和原根alpha。(在此例中訂為p = 23, alpha = 5)
2. Alice 和 Bob 分別利用 random 生成他們的私鑰 a, b，並經過 diffie_hellman() 函數計算公鑰 A,B。
```
publicKey = alpha^privateKey mod p
```
3. Alice會將其公鑰傳給Bob， Bob將其公鑰傳給Alice，再藉由compute_shared_secret() 函數計算出共享密鑰。 
```
sharedSecret = A^b mod p = B^a mod p
```
4. 使用SHA-256對共享密鑰進行hash，並取前16個字節作為AES密鑰。
5. 當Alice要傳送訊息給Bob，他會使用共享密鑰對消息進行AES-CBC加密，而Bob同樣會使用共享密鑰對加密後的信息解密。
6. encrypt()加密函數：在加密前，使用 PKCS7 將原文填充到AES塊大小(16字節)的倍數，確保資料長度符合 AES 的塊大小要求，接著使用 CBC(密碼塊鏈)模式和一個隨機生成的16字節初始化向量(IV)來加密資料。
7. decrypt()解密函數：進行相反的操作，先解密數據，再去除填充來恢復原始文本。


### 執行結果
```
Alice's Public Key:  5
Bob's Public Key:  19
Shared Secret (Alice):  19
Shared Secret (Bob):  19
Ciphertext:  b'\xfeI\x96\xdc\xce<\xa1t k-|l\xb0\xe9\xfa\x83\xf2FF\xcc\xc9\xd65\x06\xcfAf\xa2\xe2(\x0b'
Decrypted Message:  Hello, Bob!
```
