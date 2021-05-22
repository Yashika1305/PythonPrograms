num=int(input("please enter the number"))
row=0
while row<num:
	space=row
	while space>0:
		print(end="  ")
		space=space-1
	j=num-row
	k=1
	while k<=j:
		print(k,end=" ")
		k=k+1
		
	l=1
	while l<=j:
		print(l,end=" ")
		l=l+1
		
	row=row+1
	print()