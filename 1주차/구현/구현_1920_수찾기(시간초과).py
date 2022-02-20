import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int,input().split()))


n_set = set(n_list)
m_set = set(m_list)
to_be_ones = list(n_set & m_set)

print(n_list)
print(to_be_ones)

answer = []
for idx, i in enumerate(m_list):
  if str(to_be_ones).find(str(i)) == -1:
    answer.append('0')
  else:
    answer.append('1')
  
print('\n'.join(answer))

    

 



