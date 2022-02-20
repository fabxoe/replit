caesar_s = input()
l_s = list(caesar_s)
for i in range(len(l_s)):
  if l_s[i] == 'A':
    l_s[i] = 'X'    
    continue
  if l_s[i] == 'B':
    l_s[i] = 'Y'    
    continue
  if l_s[i] == 'C':
    l_s[i] = 'Z' 
    continue

  l_s[i] = chr(ord(l_s[i])-3)

print(''.join(l_s))
