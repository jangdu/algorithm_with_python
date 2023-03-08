import sys

N = int(input())

stack = []

print(1 if len(stack) == 0 else 0)

for i in range(N):
    T = sys.stdin.readline().split()
    if T[0] == 'pop':
      if len(stack) != 0:
        print(stack[len(stack)-1])
        stack.pop()
      else :
        print(-1)
    elif T[0] == 'size':
        print(len(stack))
    elif T[0] == 'empty':
      print(1 if len(stack)==0 else 0)
    elif T[0] == 'top':
        if len(stack) !=0:
          print(stack[-1])
        else: print(-1)
    else:
        stack.append(T[1])