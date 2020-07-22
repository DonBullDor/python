while True:
    print('enter your age')
    age = input()
    if age.isdecimal():
        break
    print('please enter a decimal for your age')

while True:
    print('select a new password (letter and number only)')
    password = input()
    if password.isalnum():
        break
    print('password can only have letters and numbers')
