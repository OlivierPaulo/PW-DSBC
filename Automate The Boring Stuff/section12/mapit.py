import webbrowser, sys, pyperclip

sys.argv # ['mapit.py','Rua do Conde de Redondo','91B', '1150-103 Lisboa', 'Portugal']

# Check if command Line argurments were passed
if len(sys.argv) > 1:
    # ['mapit.py','Rua do Conde de Redondo','91B', '1150-103 Lisboa', 'Portugal']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.fr/maps/place/Le+Wagon+Lisbon+Coding+Bootcamp/@38.7260907,-9.1476757,17z/data=!3m1!4b1!4m5!3m4!1s0xd19351a74f8e2a3:0x779f5b9fe8faf6a7!8m2!3d38.7260865!4d-9.145487
webbrowser.open('https://www.google.fr/maps/place/' + address)
