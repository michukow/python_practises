import random

losowa = random.randint(1,100)
proby=1
while True:
	try:
		zgadywana = int(input("Wpisz liczbę: "))
		if zgadywana==losowa:
			print("O to chodziło! Brawo!")
			print(f"Liczba prób: {proby}")
			break
		else:
			print(f"Spróbuj ponownie! Liczba prób: {proby}")
			proby+=1
			if zgadywana<losowa:
				print("Liczba o której myślę jest większa!")
			else:
				print("Liczba o której myślę jest mniejsza!")
	except Exception as e:
		print(f"Wystąpił błąd {e}!")