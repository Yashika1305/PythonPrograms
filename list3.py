#insert element at desired position 
#suppose i want to insert 11 at 2nd position
l=[1,2,3,4]
pos=2
l1=[]
l2=[]
i=0
while i<len(l):
	if(i<pos):
		l1.append(l[i])
	else:
		l2.append(l[i])
	i=i+1
l1.append(11)
print(l1+l2)