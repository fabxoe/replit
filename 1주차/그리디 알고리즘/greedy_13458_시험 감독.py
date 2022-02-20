import sys
input = sys.stdin.readline
n = int(input())
applicants = list(map(int, input().split()))
b, c = map(int, input().split())

whole_minimum_director = 0
whole_minimum_director += n
for each_room in applicants:
  each_room -= b
  
  c_director_num = each_room // c
  whole_minimum_director += c_director_num
  covered_people = c_director_num * c
  uncovered_one = each_room - covered_people

  if uncovered_one != 0:
    whole_minimum_director += 1

print(whole_minimum_director)