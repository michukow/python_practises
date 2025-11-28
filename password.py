import random

letters_small="abcdefghijklmnopqrstuvwxyz"
letters_great="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
special_chars="!#$%&'()*+,-./:;<=>?@[]^_`{|}~"

passwords: dict[str,str] = {}

def adding_password():
    while True:
        website=input("Insert website name: ").strip().lower()
        if not website:
        	print("Please insert a valid name.")
        	continue
        if website in passwords.keys():
        	print("That website exists in the database.")
        else:
        	break

    while True:
        try:
            length=int(input("Insert password length (min. 4): "))
        except ValueError:
            print("Please insert a number.")
            continue
        if length<4:
            print("Password too short. Try again.")
            continue   
        break

    chars = (
        [random.choice(letters_small) for _ in range(length-3)] +
        [random.choice(letters_great),
         random.choice(special_chars),
         random.choice(digits)]
    )

    random.shuffle(chars)
    password="".join(chars)
    passwords[website]=password
    print(f"Password for {website} set successfully!")


def show_passwords():
	if not passwords:
		print("Not passwords yet.")
	else: 
		for webiste,password in passwords.items():
			print(f"The password for {webiste} is {password}")


def search_password():
	while True:
		try:
			word=str(input("Input a website's name: "))
			if word in passwords.keys():
				print(f"Password for {word} is {passwords[word]}")
				break
			else:
				print("Not found. Try again.")
		except ValueError:
			print("Insert a valid value.")

def menu():
	print("Select an activity: ")
	print("1 - Add new password. This programme will generate new one.")
	print("2 - Show passwords.")
	print("3 - Search your password by inserting page's name.")
	print("4 - Exit.")

print("Welcome at passwords' manager")
while True:
	try:
		menu()
		x=int(input("Insert a number: "))
		if x==1:
			adding_password()
			pass
		elif x==2:
			show_passwords()
			pass
		elif x==3:
			search_password()
			pass
		elif x==4:
			break
		else:
			print("Select 1-4 option.")
	except ValueError:
		print("Insert valid value.")

