import sys
input = sys.stdin.readline
n = int(input())
for i in range(n+1):
  l = list(input().strip())
  # print(l)
  print()
  score_l=[]
  for idx, j in enumerate(l):
    # print(j)
    if j == 'O':
    #   print("1")
    # else:
    #   print("0")

      if idx == 0:
        score_l.append(1)
      else:
        if l.index(idx-1) == 'O':
          score_l.append(score_l.index(idx-1) + 1)
        else:
          score_l.append(1)
    else:
      score_l.append(0)

