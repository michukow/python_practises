def suma_parzystych(całkowite):
	suma=0
	for i in całkowite:
		if i%2==0:
			suma+=i
	return suma

print(suma_parzystych([1,2,3,5,6,89,12]))