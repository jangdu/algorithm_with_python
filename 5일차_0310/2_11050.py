n, k = map(int, input().split())


def factorial(num):
  t = 1
  for i in range(1, num+1):
    t *= i
  return t



print(factorial(n)//(factorial(k)*factorial(n-k)))