from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import hashlib
import random
import os

def diffie_hellman(p, alpha, private_key):
    # Compute public key
    public_key = pow(alpha, private_key, p)
    return public_key

def compute_shared_secret(public_key, private_key, p):
    # Compute shared secret
    shared_secret = pow(public_key, private_key, p)
    return shared_secret

# Example parameters
p = 23
alpha = 5

# Alice's private key
a = random.randint(1, p-1)
# Bob's private key
b = random.randint(1, p-1)

# Alice's public key
A = diffie_hellman(p, alpha, a)
# Bob's public key
B = diffie_hellman(p, alpha, b)

# Exchange public keys
print("Alice's Public Key: ", A)
print("Bob's Public Key: ", B)

# Compute shared secret
shared_secret_alice = compute_shared_secret(B, a, p)
shared_secret_bob = compute_shared_secret(A, b, p)

print("Shared Secret (Alice): ", shared_secret_alice)
print("Shared Secret (Bob): ", shared_secret_bob)

# Convert shared secret to a 16-byte key for AES
# We use SHA-256 to hash the shared secret and take the first 16 bytes
alice_key = hashlib.sha256(str(shared_secret_alice).encode()).digest()[:16]

def encrypt(plaintext, key):
    # Generate a random 16-byte IV
    iv = os.urandom(16)
    # Pad the plaintext to be multiple of block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    # Encrypt using AES-CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt(ciphertext, key):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    # Decrypt using AES-CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()

# Example plaintext message
message = "Hello, Bob!"

# Alice encrypts the message using the shared key
ciphertext = encrypt(message, alice_key)
print("Ciphertext: ", ciphertext)

# Bob decrypts the message using the shared key
bob_key = hashlib.sha256(str(shared_secret_bob).encode()).digest()[:16]
decrypted_message = decrypt(ciphertext, bob_key)
print("Decrypted Message: ", decrypted_message)
