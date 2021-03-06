terms=int(input("Enter number of terms for fibonacci series"))
n1=0
n2=1
 
count=0                              
while count<terms:
	if(count<=1):
		n3=count
	else:
		n3=n1+n2
		n1=n2
		n2=n3
	print(n3)
	count=count+1
	



