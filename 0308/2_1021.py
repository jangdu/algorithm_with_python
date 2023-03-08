from collections import deque


n, m = map(int, input().split())
deq = deque()
count = 0

for i in range(n):
  deq.append(i+1)

n2 = map(int, input().split())

t = deq[0]
print(deq)
for i in n2:
  num = deq.index(i)
  
  if t == deq[num]:
    deq.pop(num)