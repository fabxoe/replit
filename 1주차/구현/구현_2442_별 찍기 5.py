n = int(input())
for i in range(1, n+1):
  count=0
  for j in range(n, 0, -1):
    if j > i:
      print(" ", end="")
    else:
      print("*", end="")
      count+=1
  
  for i in range(count-1):
    print("*", end="")
    
  print()
  
   
  