i=0
n = n_origin = input()
n_i = n_i_origin = int(n_origin)

if n_i < 10:
    n = '0' + n
    n_i = int(n)

while True:
  sum = int(n[0]) + int(n[1])
  sum_str = str(sum)

  if sum < 10:
    new_n = n[1] + sum_str[0]
  else:
    new_n = n[1] + sum_str[1]
  #print("new_n: " + new_n)

  i+=1
  if n_i_origin==int(new_n): break
  n = new_n
  n_i = int(new_n)
print(i)
