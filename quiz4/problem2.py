import numpy as np
def polynomial_xor(key, text_ascii):
    result = []
    for i in range(8):
        if key[i] == text_ascii[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def char_to_ascii(char):
    ascii = ord(char)
    bin_ascii = bin(ascii)[2:].zfill(8)
    return bin_ascii

def ascii_to_char(ascii):
    ascii_value = int(ascii,2)
    char = chr(ascii_value)
    return char

def key_for_one_char(key,poly):
    key_char = ''
    for k in range(8):
        for i in range(9):
            key[i] = key[i+1]
        key_char = str(key[0])+ key_char
        key[9]=0
        for i in range(len(poly)):
            key[9] = key[9] ^ key[poly[i]]
    return key_char,key

def encrypt(plaintext, initial_key, poly):
    key = initial_key
    ciphertext = ''
    for char in plaintext:
        key_char, key = key_for_one_char(key,poly)
        ascii = char_to_ascii(char)
        ct_ascii = polynomial_xor(key_char,ascii)
        ct = ascii_to_char(ct_ascii)
        ciphertext += ct    
    return ciphertext

def decrypt(ciphertext, initial_key, poly):
    key = initial_key
    plaintext = ''
    for char in ciphertext:
        key_char, key = key_for_one_char(key,poly)
        ascii = char_to_ascii(char)
        pt_ascii = polynomial_xor(key_char,ascii)
        pt = ascii_to_char(pt_ascii)
        plaintext += pt 
    return plaintext

def linear(ciphertext):
    # not finished T_T
    plaintext = ''
    ct_ascii = ''
    for i in range(2):
        ct_ascii = char_to_ascii(ciphertext[i]) + ct_ascii
    print(ct_ascii)
    coefficients = []
    for i in range(8):
        lst = []
        for j in range(8):
            lst.append(int(ct_ascii[i+j+1]))
        coefficients.append(lst)
    coefficients = np.array(coefficients)
    constants = []
    print(coefficients)
    for i in range(8):
        constants.append(int(ct_ascii[i]))
    constants = np.array(constants)
    print(constants)
    solution = np.linalg.solve(coefficients, constants) %2
    print("Solution:", solution)

plaintext = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE"
initial_key = [0,1,0,0,0,0,0,0,0,0]
poly = [0,2,3,4,8]

# Encrypt plaintext
encrypted_message = encrypt(plaintext, initial_key, poly)
print("Encrypted message:\n", encrypted_message)

initial_key = [0,1,0,0,0,0,0,0,0,0]
# Decrypt ciphertext
decrypted_message = decrypt(encrypted_message, initial_key, poly)
print("Decrypted message:\n", decrypted_message)
