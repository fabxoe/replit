import sys
input = sys.stdin.readline
n, k = map(int, input().split())

coin_types=[]
for i in range(n):
  coin_types.append(int(input().strip()))
coin_types.sort(reverse=True)

count = 0
target = k
for coin_type in coin_types:
  if coin_type > target: 
    continue
  
  quotient = (target // coin_type)
  target -= (quotient * coin_type)
  count += quotient
  
print(count)