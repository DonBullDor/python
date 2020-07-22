catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) + '(or enter nothing to stop): ')
    names = input()
    if names == '':
        break
    catNames += [names]  # list concatenation

print('the cat names are :')
for name in catNames:
    print(" " + name)
