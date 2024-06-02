# instagram :- @0aritrasa1
import string
import random
import time
from colorama import *

init()

def color():
	print(Style.RESET_ALL)

def exit():
	time.sleep(1)
	sys.exit()

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print(f"{Fore.CYAN}Press X to exit")
color()
time.sleep(0.5)


while True:
	pass_len = int(input(f"\n{Fore.RED}Enter the length of pass  :   "))
	if pass_len == 'x':
		exit()
	else:
		pass	
	color()
	gen_pass =generate_password(pass_len)
	print("\n",Fore.GREEN+gen_pass)
