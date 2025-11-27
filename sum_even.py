#2 - sum even numbers
def suma_parzystych(całkowite):
	suma=0
	for i in całkowite:
		if i%2==0:
			suma+=i
	return suma

print(suma_parzystych([1,2,3,5,6,89,12]))

print("---------------")

#3 - quotient
def oblicz_iloraz(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		return "Błąd: Dzielenie przez zero!"

print(oblicz_iloraz(10, 2))
print(oblicz_iloraz(5, 0))


