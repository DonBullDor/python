birthdays = {'alice': 'Apr 1', 'bob': 'Dec 12', 'carol': 'Mar 4'}

while True:
    print('enter a name (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("not found, search by birthday ")
        bDay = input()
        birthdays[name] = bDay
        print('birthday database updated !')
