
a = "472"
b = "385"
a = int(a)
b = list(b)
whole = 0
for each_b in b:
    each_value = a * int(each_b)
    print(each_value)
    whole += each_value

print(whole)