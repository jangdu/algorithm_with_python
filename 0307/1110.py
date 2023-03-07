# 26 => 2 + 6 => 8
# 68 => 6 + 8 => 14
# 84 => 8 + 4 => 12
# 42 => 4 + 2 => 6
# 26

num = int(input())
sum = 0
count = 0
temp = num

while True:
  a = temp//10
  b = temp%10
  sum = a + b
  temp = b * 10 + sum%10
  count += 1
  if temp==num:
    break

print ( count )