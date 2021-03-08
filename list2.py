#split list into two parts  from specified position
l=[1,3,2,6,7,8]
pos=4
l1=[]
l2=[]
i=0
while i<len(l):

	if(i<pos):
		l1.append(l[i])
	else:
		l2.append(l[i])
	i=i+1
print(l1)
print(l2)
