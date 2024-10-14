


import random
import string
import time
import sys




def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print(f"Press X to exit")
time.sleep(0.5)


while True:
	pass_len = input(f"\nEnter the length of pass  :   ")
	if pass_len.lower() == "x":
		sys.exit(0)
		
	else:
		try:
		    pass_len = int(pass_len)
		    gen_pass =generate_password(pass_len)
		    print("\n",gen_pass)
		
		except:
		    print("only int are allowed!")
		    		    
