row=int(input("Enter the no of rows"))
i=1
while i<row:
	space=row-i-1
	while space>0:
		print(end=" ")
		space=space-1
	star=i
	while star>0:
		print("*",end=" ")
		star=star-1
	
	i=i+1
	print()