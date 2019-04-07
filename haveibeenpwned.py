# Importing libraries
import json, time, sys, requests
from termcolor import colored, cprint
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--password", help="Check if password has been pwned")
parser.add_argument("-e", "--email", help="Check if email has been pwned")
args = parser.parse_args()

def password(password:str=None):
	# User input
	if password is None:
		password = input("Enter a password> ")
	else:
		password = args.password
	
	hash = hashlib.sha1(password.encode()).hexdigest()
	prefix = hash[0:5]
	suffix = hash[5:].upper()
	
	# Sents request to the haveibeenpwned api (https://haveibeenpwned.com/api/v2)
	r = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
	content = r.content.decode()
	lines = content.replace('\r', '').split('\n')

	pwned = None

	for line in lines:
		info = line.split(':')
		if info[0] == suffix:
			pwned = info[1]
			break
		
	if pwned is None:
		print("You're not pwned! Yay :)")
	else:
		print(f"You've been pwned {pwned} times :(")

def email(email:str=None):
	# User input
	if email is None:
		email = input(colored("Enter a email\n", attrs=['bold']))
	else:
		email = args.email
	# Sents request to the haveibeenpwned api (https://haveibeenpwned.com/api/v2)
	r = requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{email}')
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

if not args.password is None:
	password(args.password)
elif not args.email is None:
	email(args.email)
else:
	#if __name__ == '__main__':
	print("Choose below:")
	print("1. Email")
	print("2. Password")
	print("3. About")
	menuinput = input("> ")

	if menuinput == "1":
		email()
	elif menuinput == "2":
		password()
	elif menuinput == "3":
		cprint("About:", attrs=["bold"])
		print("Password:\nThe password gets hashed using sha1, and then only sents the first 5 characters to the API. The API returns the suffix and number of times it has been pwned.\n")

		print("Made by viggo\nAnd a little help from dnorhoj :)\n")
	else:
		print("Error!")

