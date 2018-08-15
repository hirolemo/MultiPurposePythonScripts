#! python3
#textreq.py
import requests, sys

#res (Response object) res.status_code == requests.code.ok (True if download succeeded)

# easier way is to: res.raise_for_status()
# ^ raises Exception on response object for errors] stops as soon as detected
#**^ if error is not a deal breaker, wrap in raise_for_status with try/except statements to handle

#Code add-ons
''' try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc)) (exc == 404 Client Error: Not Found
        so 'exc' is the error pulled from the web page'''

if len(sys.argv) > 1:
    #get address from command line
    address = ' '.join(sys.argv[1:])

res = requests.get(address)
res.raise_for_status() # stops program if error in downloading

playFile = open('new_file_name.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close

