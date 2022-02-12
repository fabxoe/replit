is_leap_year = 0
year = int(input())

if ((year % 4) == 0 and ((year % 100) != 0) or (year % 400) == 0):
  is_leap_year = 1

print(is_leap_year)
