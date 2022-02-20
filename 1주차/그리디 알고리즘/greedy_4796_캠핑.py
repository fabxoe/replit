import sys
input = sys.stdin.readline
#L = 10     5
#P = 20     8
#V = 28     20

case=0
while True:
  L, P, V = map(int, input().rstrip().split())
  case += 1
  if L == 0 and P == 0 and V == 0:
    break

  # whole_reserved_period = repeat_count * P
  # remain_days = V - whole_reserved_period
  repeat_count = V // P
  remain_days = V % P
  continuous_camp_day = repeat_count * L

  if remain_days >= L:
    continuous_camp_day += L
  if remain_days < L:
    continuous_camp_day += remain_days

  print("Case {}: {}".format(case, continuous_camp_day))