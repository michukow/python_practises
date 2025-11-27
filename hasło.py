import string
male_litery = string.ascii_lowercase
duze_litery = string.ascii_uppercase
cyfry = "1234567890"
znaki_sepcjalne = "!@#$%^&*()-_+=|,./';[]{}:?><"

def hasło(tekst):
	pkt=0
	if len(tekst)>7:
		pkt+=1
	for litera in tekst:
		if litera in male_litery:
			pkt+=1
			print("Twoje hasło zawiera małą literę!")
		elif litera in duze_litery:
			pkt+=1
			print("Twoje hasło zawiera dużą literę!")
		elif litera in cyfry:
			pkt+=1
			print("Twoje hasło zawiera cyfrę!")
		elif litera in znaki_sepcjalne:
			pkt+=1
			print("Twoje hasło zawiera znak specjalny!")
	print(f"Zdobyłeś {pkt}")
	if pkt>1 and pkt<2:
		print("Tragedia!")
	elif pkt>2 and pkt<3:
		print("Twoje może być, ale bez szału")
	elif pkt==4:
		print("Dobre!")
	else:
		print("Brawo, pancerniku!")

hasło("MarysiaJestSuper")



