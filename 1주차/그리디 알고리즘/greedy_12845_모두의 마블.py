import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().rstrip().split()))

L.sort(reverse = True)

level_memo = 0
gold = 0
for idx, level in enumerate(L):
  if idx == 0:
    level_memo = level
    continue
  
  gold += level_memo + level

  print(level_memo)
  if level_memo < level:
    level_memo = level

print(gold)