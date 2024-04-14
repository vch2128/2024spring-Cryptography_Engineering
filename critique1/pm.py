import psycopg2
from cryptography .hazmat.primitives import hashes 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
from cryptography.hazmat. backends import default_backend 
from cryptography.fernet import Fernet
import base64

def derive_encryption_key (master_password,salt):
    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256(), 
        length=32, 
        salt=salt, 
        iterations=100000, 
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

def encrypt(pwd,key):
    fernet = Fernet(key)
    encrypted_pwd = fernet.encrypt(pwd.encode())
    return encrypted_pwd

def decrypt(encrypted_pwd,key):
    fernet = Fernet(key)
    decrypted_pwd = fernet.decrypt(encrypted_pwd).decode()
    return decrypted_pwd 

def search(cur,domain):
    sql = "SELECT * FROM pwds WHERE domain = '{}'".format(domain)
    cur.execute(sql)
    rows =  cur.fetchall()
    return rows

def insert(conn,cur):
    domain = input("Domain:")
    id = input("ID:")
    pwd = input("Password:")
    sql = "INSERT INTO pwds (domain,id,pwd) VALUES (%s,%s,%s)"
    cur.execute(sql,(domain,id,pwd))
    conn.commit()
    print("Insert successful.")

def create_manager(conn,cur):
    name = input("Name:")
    pwd = input("Password:")
    key = derive_encryption_key(pwd,name.encode('utf-8'))
    sql = "INSERT INTO managers (name,pwd,key) VALUES (%s,%s,%s)"
    cur.execute(sql,(name,pwd,key))
    conn.commit()
    print("Create manager successful.")

def search_manager(cur,pwd):
    sql = "SELECT * FROM managers WHERE pwd = '{}'".format(pwd)
    cur.execute(sql)
    rows =  cur.fetchall()
    return rows

def main():
    master_pwd = "1234"
    mpwd = input("Enter your manager password:")
    conn = psycopg2.connect(
            dbname="pwdmanager",
            user="tinghsinchuang",
            password="",
            host="localhost",
            port="5432"
        )
    cur = conn.cursor()
    data = search_manager(cur,mpwd)
    if data == []:
        op = input("Manager not found. Create? (y/n) ")
        if op =='y':
            master = input("Enter master password:")
            if master == master_pwd:
                create_manager(conn,cur)
            else:
                print("Wrong password. End program.")
        else:
            print("End program.")

    # if master != manager_pwd:
    #     print("Wrong password.")
    # else:
    #     conn = psycopg2.connect(
    #         dbname="pwdmanage",
    #         user="tinghsinchuang",
    #         password="vanessa1315",
    #         host="localhost",
    #         port="5432"
    #     )
    #     cur = conn.cursor()
    #     print("Connected to the database.")


if __name__ == "__main__":
    main()



