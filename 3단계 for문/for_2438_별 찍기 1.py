import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
  for j in range(1, i+1):
    print("*", end="")
  print()