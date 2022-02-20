import sys
input = sys.stdin.readline

k = int(input())

endurance_rope = []
for i in range(k):
  endurance_rope.append(int(input().rstrip()))

endurance_rope.sort(reverse=True)

max_endurance = 0
for ea, each_endurance in enumerate(endurance_rope):
  ea += 1
  if ea == 1:
    max_endurance = each_endurance
    continue

  parallel_endurance = ea * each_endurance
  if max_endurance < parallel_endurance:
    max_endurance = parallel_endurance
  
print(max_endurance)


