l=[]
l.append(11)
l.append(4)
l.append(86)
l.append(9)
l.append(134)
l.append(25)
l.append(22)
print(l)
minimum=l[0]
i=0
while i<len(l):
	if l[i]<minimum:
		minimum=l[i]
	i=i+1	
print(minimum)	
maximum=l[0]
j=0		
while j<len(l):
	if l[j]>maximum:
		maximum=l[j]
	j=j+1	
print(maximum)