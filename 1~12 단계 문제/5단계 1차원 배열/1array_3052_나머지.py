import sys
from collections import Counter

input = sys.stdin.readline
l = []
for i in range(10): 
  l.append(int(input()) % 42)

print(len(Counter(l)))
