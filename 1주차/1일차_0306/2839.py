number = int(input())
count = 0

if number % 5 == 0:
    count = number//5
elif number > 2:
  while number >= 0:
    if number % 5 == 0:
      count += number // 5
      break
    number -= 3
    count += 1
  else: count = -1
else:
   count = -1

print(count)