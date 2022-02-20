import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
  t_case = int(input().strip())
  reversed_bi_memo = []
  while True:
    reversed_bi_memo.append(t_case % 2)
     
    if t_case // 2 == 0:
      break

    t_case //= 2
  
  for idx, i in enumerate(reversed_bi_memo):
    if i == 1:
      print(idx, end=" ")
