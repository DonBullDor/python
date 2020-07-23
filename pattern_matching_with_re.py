import re

phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumber.search('my phone number is  415-555-4242.')
#print(mo.group(1))
#print(mo.group(2))
#print(mo.group(0))

#print(mo.groups())

areaCode, mainNumber = mo.groups()
#print(areaCode)
#print(mainNumber)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#print(mo1)

xmasRegex = re.compile(r'\d+\s\w+')
mo2 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
#print(mo2)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo3 = nameRegex.search('First Name: Al Last Name: Sweigart')
#print(mo3)

nongreedyRegex = re.compile(r'<.*>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
#print(mo)

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#print(mo)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1*******', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)
