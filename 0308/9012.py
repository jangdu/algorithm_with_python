


n = int(input())
result = ''

for _ in range(n):
    stack = []  
    str = input()
    for i in str:
      if i == '(':
        stack.append(i)
      elif i == ')':
        if len(stack) == 0:
          print('NO')
          break
        else:
          stack.pop()
    else:
      if len(stack)==0:
          print("YES")
      else:
          print("NO")
