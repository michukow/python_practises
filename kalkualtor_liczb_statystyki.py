def kalkulator(liczby):
	suma=0
	x=0
	try:
		lista=[]
		lista=liczby.split()
		for i in lista:
			i=int(i)
			suma+=i
		print(f"Suma wynosi {suma}")
		print(f"Srednia wynosi {suma/len(lista)}")
		print(f"Maksimum wynosi: {max(lista)}")
		print(f"Minimum wynosi: {min(lista)}")
		for i in lista:
			if int(i)>(suma/len(lista)):
				x+=1
		print(f"Liczba elementów, która jest większa od średniej, czyli {suma/len(lista)} to {x}")
	except Exception as e:
		print(e)

kalkulator("1 2 3")