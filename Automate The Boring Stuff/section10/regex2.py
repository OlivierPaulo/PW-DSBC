import re
phoneNumRegex =re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 425-555-9090')

print(f"{mo.group()}")
print(f"{mo.group(1)}")
print(f"{mo.group(2)}")
