def def e(a):
	x=a
	e=(1+1/x)**x
	return float(e)


h=(int(input("Write the bumber of decimal points")))

k = e(h)


print("The estimate of the constant e is",k)
