n = int(input())
l = list(map(int, input().split()))

max_num = 0;
min_num = 0;
for idx, i in enumerate(l):
  if idx==0:
    max_num = min_num = i
    continue

  if max_num < i:
    max_num = i

  if min_num > i:
    min_num = i 

print("{} {}".format(min_num, max_num))

