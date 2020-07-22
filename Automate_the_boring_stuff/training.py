from builtins import print

print('Hello world!')
print('What is your name?')  # ask for their name
myName = input()
if myName == "med":
    print('It is good to meet you, ' + myName)
else:
    print("who are you bro")
    print('The length of your name is:')
    print(len(myName))
    print('What is your age?')  # ask for their age
    myAge = input()
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    print("end !!")