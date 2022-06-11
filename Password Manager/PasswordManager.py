import os
from posixpath import dirname
from cryptography.fernet import Fernet

present_dir = os.path.dirname(os.path.realpath(__file__))

'''
def write_key():
    key = Fernet.generate_key()
    filepath = os.path.join(present_dir, 'key.key')
    with open(filepath, "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    filepath = os.path.join(present_dir, 'key.key')
    file = open(filepath, "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    filepath = os.path.join(present_dir, 'passwords.txt')
    with open(filepath, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password= data.split("|")
            print("Username : ",user, "| Password :", fer.decrypt(password.encode()).decode())

def add():
    name = input("Account Name: ")
    password = input("Password: ")
    filepath = os.path.join(present_dir, 'passwords.txt')
    with open(filepath, 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode =  input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
        continue