### To review as is not working properly

import re

powerReg = re.compile(r"""
(((\d\d\d-)|(\(\d\d\d-)))?     # area code of phone number (without parentheses -or- area code with parentheses and no dash
\d\d\d                       # first 3 digits
-                            # second dash
\d\d\d\d                     # last 4 digits
""",re.IGNORECASE | re.DOTALL | re.VERBOSE)

phone = "444-555-6666"
print(powerReg.search(phone))