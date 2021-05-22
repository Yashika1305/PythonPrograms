def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

t=fact(4)
print(t)

