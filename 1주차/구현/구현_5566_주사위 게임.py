import sys
input = sys.stdin.readline

n, m = map(int, input().split())

game_map = []
for i in range(n):
  game_map.append(int(input().rstrip()))

dice = []
for i in range(m):
  dice.append(int(input().rstrip()))


position=0
length_of_game_map = len(game_map)
dice.reverse()
dice_rolling_counter = 0

for i in range(m):

  dice_num = int(dice.pop())
  dice_rolling_counter += 1
  position += dice_num

  if (position >= length_of_game_map) or (position + game_map[position] >= length_of_game_map):
    break

  position += game_map[position]

print(dice_rolling_counter)