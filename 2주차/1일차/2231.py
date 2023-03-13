def sumOfDigits(num):
    digits = map(int, list(str(num)))
    return (sum(digits))

n = int(input())

num = 0

for i in range(n):
    num = i + sumOfDigits(i)
    print(num)
    if num == n :
      print(i)
      break
else:
    print(0)


