
a = "472"
b = "385"
a = int(a)
b = list(reversed(b))
whole = 0
for i, each_b in enumerate(b):
    each_value = a * int(each_b)
    print(each_value)
    whole += each_value * (10 ** i)

print(whole)