#Greetings

name = input('Enter a name : ')

if name.upper() == 'TRAN':
    password = input('Please enter your password : ')
    if password == 'secret':
        print('Hello Master')
    else:
        print('IMPOSTER')
else:
    print('Who are you?')
