import sys
input = sys.stdin.readline
n = int(input())

l = list(map(int, input().split()))
l.sort()

waiting_time = 0
whole_time = 0
for action_time in l:
  waiting_time += action_time
  whole_time += waiting_time 

print(whole_time)