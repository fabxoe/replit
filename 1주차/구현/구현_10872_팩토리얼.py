def pactorial(p):
  if p == 1 or p == 0 :
    return 1
  return p * pactorial(p - 1)

n = int(input())
print(pactorial(n))