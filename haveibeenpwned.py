# Importing libraries
import json, time, sys, requests
from termcolor import colored, cprint
import hashlib

def password():
    # User input
    password = input("Enter a password. \n")
    hash = hashlib.sha1(password.encode()).hexdigest()
    hashed = hash[0:5]
    print(hashed)
    
    # Sents request to the haveibeenpwned api (https://haveibeenpwned.com/api/v2)
    r = requests.get('https://api.pwnedpasswords.com/range/' + hashed)
    # Checks the status code. 200 
    if r.status_code is 200:
        cprint("Your password have been pwned.", "red")
    else:
        cprint("Your password have not been pwned, ;)", "green")
    exit()

def email():
    # User input
    user = input(colored("Enter a email\n", attrs=['bold']))
    # Sents request to the haveibeenpwned api (https://haveibeenpwned.com/api/v2)
    r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + user)
    # Checks the status code. 200 
    if r.status_code is 200:
        cprint("You have been pwned.\n", "red")
        unload_json = r.text
        load_json = json.loads(unload_json)
        cprint("Your email have been leaked on the following sites:", "blue", attrs=['bold'])
        for x in range (0, (len(load_json))):
            cprint(colored(load_json[x]['Title'], "magenta"))
    else:
        cprint("You have not been pwned, ;)", "green")
    x = 1
    exit()

def menu():
    print("Choose below:")
    print("1. Email")
    print("2. Password")
    print("3. About")
    menuinput = input("> ")

    if menuinput == "1":
        email()
    elif menuinput == "2":
        password()
    else:
        print("Fejl!")

menu()
