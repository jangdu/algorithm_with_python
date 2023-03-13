n = int(input())

money = []


money = list(map(int, input().split()))


money.sort()

sum = 0
result = 0
for i in money:
  sum += i
  result += sum

print(result)