import sys
input = sys.stdin.readline

n = int(input())


for i in range(n):
  a,b = map(int, input().rstrip().split())
  gcd=0

  a_memo = a
  b_memo = b
  while b_memo!=0:
  
    r = a_memo % b_memo
    a_memo = b_memo
    b_memo = r
    gcd = a_memo
 
  print((a * b)//gcd)
  
  
   



