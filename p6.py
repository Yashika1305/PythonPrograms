i=0
j=0
while i<7:
	while j<=i:
		if(j==0 or j%3==0):
			print("*****",end=" ")
		else:
			print("*",end=" ")
		j=j+1

	print()
	i=i+1