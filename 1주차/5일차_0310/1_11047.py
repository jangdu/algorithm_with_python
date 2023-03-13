import collections

N, sum = map(int, input().split())

deq = collections.deque([])
coin = []
for i in range(N):
  deq.appendleft(input())
for i in reversed(range(N)):
  a = 0

# for i in range(num, 0, -1): 반대로
print(deq)

# 11047

# n, k = map(int, input().split())
# num = []

# count = 0
# for i in range(n):
#   num.append(int(input()))
  
# num = list(reversed(num))

# for i in range(len(num)):
#   count += k // num[i]
#   k = k % num[i]
  
# print(count)


# 11047

# n, k = map(int, input().split())
# num = []

# count = 0
# for i in range(n):
#   num.append(int(input()))
  
# num.reverse()

# for i in range(len(num)):
#   count += k // num[i]
#   k = k % num[i]
  
# print(count)