lt = [(1, 2), (4, 5), (7,6)] 
  
out = [item for t in lt for item in t] 
  

print(out) 
lt[1]=100
print(out)
