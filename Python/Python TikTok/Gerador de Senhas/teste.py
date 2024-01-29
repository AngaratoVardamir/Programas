import random
print('Sua Senha: ')
Chars = '!@#$%¨&*()1234567890QWERTYUIOPASDFGHJKLÇZXCVBNMqwertyuiopasdfghjklçzxcvbnm'
password = ''
for X in range(16):
    password += random.choice(Chars)
print(password)