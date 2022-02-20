import sys

input = sys.stdin.readline
l = []
for i in range(9):
  l.append(int(input().strip()))

max_num = max(l)
ordinal_n = l.index(max_num) + 1

print(max_num)
print(ordinal_n)
