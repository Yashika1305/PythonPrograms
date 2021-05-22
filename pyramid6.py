row=int(input("enter the no of rows"))
i=1
while i<row:
	space=row-i-1
	while space>0:
		print(end="  ")
		space=space-1
	num=i
	j=1
	while j<=num:
		print(j,end=" ")
		j=j+1
	k=i-1
	while k>0:
		print(k,end=" ")
		k=k-1
	i=i+1
	print()