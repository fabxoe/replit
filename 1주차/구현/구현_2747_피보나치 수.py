n = int(input())

pivonachi = [0, 1, 1]
count = 0
while True:

  if count > 2:
    pivonachi.append(
      pivonachi[count-2] + pivonachi[count-1]
    )

  if count == n:
    break
    
  count += 1

print(pivonachi[n])


