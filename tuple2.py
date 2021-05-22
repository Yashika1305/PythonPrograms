#tuple is immutable
#tuple allows slicing

t=(0,1,2,3,4,5,6)
print(t[1:])
#reverse
print(t[::-1])

print(t[2:5])

print(len(t))

del t
print(t) #error t not defined because it is deleted