#sum function
#sum only takes number value else give type error
l=[1,2,3,4,5,1,2,4,5,3,1,3,2,3,1,4]
print(sum(l))

print('*************')

#count the occurrence of a given element
print(l.count(1)) 
print(l.count(2))
print(l.count(3))

print('*************')

#length of list
print(len(l))

#index fuction is used to return the first occurence of element
print(l.index(1))
#return index of nth occurence of element
print(l.index(3,3))