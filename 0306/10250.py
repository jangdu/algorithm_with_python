t = int(input())
f = 0
for i in range (0,t):
  h,w,n = map(int, input().split())
  f = (h%n) * 100 + (n//h) + 1
  print (f)