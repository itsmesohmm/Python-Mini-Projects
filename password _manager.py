from cryptography.fernet import Fernet
import os
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)
'''
def load_key():
   file = open('key.key','rb')
   key = file.read()
   file.close()
   return key'''


def load_key():
    if not os.path.exists('key.key'):
        write_key()  
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key


key = load_key() 
fer = Fernet(key)


def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print('User: ',user,'| Password:',fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    mode =input('Would u like to add a new password or view the existing ones?(view/add),press q to quit').lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid mode')
        continue