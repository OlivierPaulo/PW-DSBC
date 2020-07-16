#! python3

import re, pyperclip
import math

# Create a regex for phone numbers
## => What's expected as phone numbers : 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

phoneReg = re.compile(r'''

(((\d\d\d)|(\(\d\d\d\)))?     # Area code could be optional
(\s|-)                      # first seperator                
\d\d\d                      # three digits
-                           # first/second dash
\d\d\d\d                    # the following 4 digits
(((ext(\.)?\s)|x)            # ext(.) (optional)
(\d\d\d\d\d))?)               # (x)12345 (optional)  ###To check HERE if error###
''', re.VERBOSE)


##print(phoneReg.search('455-666-7777'))
#print(phoneReg.findall('(415) 555-0000 ext 12345'))

# Create a regex for emails addresses
## => What's expected as email adresses : some._-thing@domain-word.com

emailReg = re.compile(r'''

[a-zA-Z0-9-_.+]+    # handle name with .,-,_ as optional
@                                     # contains @ between name and domain
[a-zA-Z0-9-_.+]+    # manage domain
             
''', re.VERBOSE)

##print(emailReg.search("test-test@test-group.fr"))

# Create to get text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = phoneReg.findall(text)
extractedEmail = emailReg.findall(text)

allPhoneNumber = []
for phoneNumber in extractedPhone:
    allPhoneNumber.append(phoneNumber[0])


print(allPhoneNumber)
print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = {}

for i in range(max(len(extractedEmail),len(allPhoneNumber))):
    results[extractedEmail[i]]=allPhoneNumber[i]


#result = '\n'.join(extractedEmail) + ' : ' + '\n'.join(allPhoneNumber)
pyperclip.copy(str(results))