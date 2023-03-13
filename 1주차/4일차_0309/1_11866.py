# sep(), end()

from collections import deque


n, m = map(int, input().split())

deque = deque(range(1, n+1))
result = []

# deque.rotate(x) -> if x > 0: deque 오른쪽으로 shift
#                    if x < 0: deque 왼쪽으로 shift

# 1 2 3 => 3. m - 1
while len(deque) != 0:
  
  deque.rotate(-(m-1))
  result.append(deque.popleft())

print('<', end='')
[print( i, end=', ' if i != result[-1] else '>\n') for i in result]


