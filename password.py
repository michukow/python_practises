import random

letters_small="abcdefghijklmnopqrstuvwxyz"
letters_great="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
special_chars="!#$%&'()*+,-./:;<=>?@[]^_`{|}~"

passwords = {}

def adding_password():
	while True:
		try:
			webiste=str(input("Insert a name of webiste: "))
			try:
				n=int(input("Insert a length of password: "))
				if n<4:
					print("Select a number greater or equal than 4")
				else:
					print("Trying to set safe password")
					password=""
					for i in range (n):
						password+=random.choice(letters_small)
					password+=random.choice(letters_great)+random.choice(special_chars)+random.choice(digits)
					passwords[webiste]=password

					print("Your password was set.")
					break
			except ValueError:
				print("Insert valid value.")
		except ValueError:
			print("Insert valid value.")

def show_passwords():
	for webiste,password in passwords.items():
		print(f"The password for {webiste} is {password}")

def search_password():
	while True:
		try:
			word=str(input("Input a webiste's name: "))
			if word in passwords.keys():
				print(f"Password for {word} is {passwords[word]}")
				break
			else:
				print("Not found. Try again.")
		except ValueError:
			print("Insert a valid value.")

print("Welcome at passwords' manager")
print("Select an activity: ")
print("1 - Add new password. This programme will generate new one.")
print("2 - Show passwords.")
print("3 - Search your password by inserting page's name.")
print("4 - Exit.")

while True:
	try:
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

