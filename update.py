d1={1:2,2:3,4:78}
d2={1:3,2:8,4:7}
sum=0
for i in d1:
	for j in d2:
		if(i==j):
			sum=d1[i]+d2[j]
	print(sum)
		