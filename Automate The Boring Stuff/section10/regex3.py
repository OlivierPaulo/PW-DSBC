import re

beginReg = re.compile(r'^Hello')
message = "Bonjour je suis Olivier"
sentence = "Hello, I am Olivier"

print(beginReg.search(message))
print(beginReg.search(sentence))

endReg = re.compile(r'Olivier$')

print(endReg.search(message))
print(endReg.search(sentence))

alldigit = re.compile(r'^\d+$')

numbers1 = '23953495734937493'
numbers2 = '23953495x734937493'

print(alldigit.search(numbers1))
print(alldigit.search(numbers2))

atReg = re.compile(r'.at')
new_mess = 'The cat in the hat sat on the flat mat.'

print(atReg.findall(new_mess))

atReg2 = re.compile(r'.{1,2}at')

print(atReg2.findall(new_mess))

name_intro = 'First Name: Olivier Last Name: Paulo'

nameReg = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameReg.findall(name_intro))

serve = '<to serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust.\n Protect the innocent.\nUpload the law'
print(prime)

dotStart = re.compile(r'(.*)')
print(dotStart.search(prime))

dotStart2 = re.compile(r'.*',re.DOTALL)
print(dotStart2.search(prime))

vowelReg = re.compile(r'[aeiouy]', re.I)
print(vowelReg.findall(prime))



