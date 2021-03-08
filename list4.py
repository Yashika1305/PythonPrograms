#if element is present in both the list, append it into new list
l1=[1,2,4,5,6,7]
l2=[4,5,6,7,8,9]
l3=[]
i=0
#while i<len(l1):
#	j=0
#	while j<len(l2):
#		if(l1[i]==l2[j]):
#			l3.append(l1[i])
#		j=j+1
#	i=i+1	
#print(l3)


while i<len(l1):
	if l1[i] in l2:
		l3.append(l1[i])
	i=i+1
print(l3)



