#generate list without duplicates
l=[1,2,4,5,3,2,4,5]
l1=[]
i=0
while i<len(l):
	ele=l[i]
	if ele not in l:
		l1.append(ele)
	i=i+1
print(l1)	

#s=set(l)
#print(s)
#l1=list(s)
#print(l1)