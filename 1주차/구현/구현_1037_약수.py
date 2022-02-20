n = int(input())
real_divisors = list(map(int,(input().split())))
print(min(real_divisors) * max(real_divisors))