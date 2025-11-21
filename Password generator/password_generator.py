import random as r
import string as s

t = s.ascii_letters + '!@#$%^&*()][{}_+'

while True:
    print('Welcome to Password Generator')
    le = input('length: ')
    password = ''.join(r.sample(t, int(le)))
    print(password)
