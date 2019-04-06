# Importing libraries
import json, time, sys, requests
# Colors
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# User input
user = input(colors.BOLD + "Enter a email. \n" + colors.ENDC)
# Sents request to the haveibeenpwned api (https://haveibeenpwned.com/api/v2)
r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + user)
# Checks the status code. 200 
if r.status_code is 200:
    print(colors.FAIL + "You have been pwned." + colors.ENDC)
    unload_json = r.text
    load_json = json.loads(unload_json)
    print(colors.OKBLUE + "Your email have been leaked on the following sites:" + colors.ENDC)
    for x in range (0, (len(load_json))):
        print(colors.HEADER + load_json[x]['Title'] + colors.ENDC)
else:
    print(colors.OKGREEN + "You have not been pwned, ;)" + colors.ENDC)
x = 1
exit()

