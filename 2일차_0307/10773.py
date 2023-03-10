import sys
num = sys.stdin.readline()

money = []
total = 0
for i in range(num):
  t = sys.stdin.readline()
  if i == 0:
    money.append(t)
    total+=t
  else:
    if t==0:
      total -= money[len(money)-1]
      money.pop()
    else:
      money.append(t)
      total += money[len(money)-1]

  

print(total)