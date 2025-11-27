def file_operations(cos):
	with open (cos,'r') as file:
		txt = file.readlines()
	return len(txt)

print(file_operations("test.txt"))
#i don't know if it works
