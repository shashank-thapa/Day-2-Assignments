import re

password_sequence = input('Enter a password: ')

pattern = r'[A-Za-z0-9@#$%^&+=]+.{8,}'

if (re.match(pattern,password_sequence)):
    print('Match')
else:
    print('Not match')