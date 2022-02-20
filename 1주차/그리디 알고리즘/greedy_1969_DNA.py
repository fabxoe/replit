import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dnas = []
for i in range(n):
  dnas.append(list(input().rstrip()))

good_dna = []
marker = {}
for i in range(m):
  marker = {'A':0, 'C':0, 'G':0, 'T':0 }
  for j in range(n): 
    if dnas[j][i] == 'A':
      marker['A'] = int(marker['A']) + 1
    
    if dnas[j][i] == 'C':
      marker['C'] = int(marker['C']) + 1
    
    if dnas[j][i] == 'G':
      marker['G'] = int(marker['G']) + 1
    
    if dnas[j][i] == 'T':
      marker['T'] = int(marker['T']) + 1
  good_dna.append(max(marker, key=marker.get))
print(''.join(good_dna))

hamming_distance_count = 0
for i in range(m):
  for j in range(n):
    if dnas[j][i] != good_dna[i]:
      hamming_distance_count += 1
print(hamming_distance_count)

  
