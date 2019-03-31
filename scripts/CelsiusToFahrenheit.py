def CelsiusToF(c):
	return (1.8 * c) + 32
	
c = input("enter celsius")
c = float(c)
f = CelsiusToF(c)
print(f)
