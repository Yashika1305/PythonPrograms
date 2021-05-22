#convert list ,string to tuple

l=[0,1,3,4]
print(tuple(l))
print(tuple('python'))


#forloop
t1=('geeks',)
n=5
for i in range(int(n)):
	t1=(t1,)
	print(t1)