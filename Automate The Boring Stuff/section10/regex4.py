import re

character = "Agent Alice gave the secret documents to Agent Bob"

namesReg = re.compile(r'Agent \w+')
print(namesReg.findall(character))

print(namesReg.sub('REDACTED',character))


nameReg2 = re.compile(r'Agent (\w)\w*')
print(nameReg2.findall(character))

print(nameReg2.sub(r'Agent \1****',character))

