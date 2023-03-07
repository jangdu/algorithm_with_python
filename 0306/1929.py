m, n = map(int, input().split())

def prime(x):
  for i in range(2,x):
      if x % i == 0:
          return False
  return True

for i in range (m, n) :
  if prime(i):
    print(i)
    