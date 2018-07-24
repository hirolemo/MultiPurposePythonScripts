#! python3 
#mapIt.py

#^ to run from command line

import webbrowser, sys
if len(sys.argv) > 1:
    #get address from command line
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
