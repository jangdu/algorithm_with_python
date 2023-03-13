
a=(input().split('-'))

result = []
# ['50', '50', '50+50']

for i in (a):
  # find()
  plus = 0
  b = (i.split('+'))  # ['50', '50']
  for j in b:
    plus += int(j)
  result.append(plus)
n = result[0]
for i in range(1, len(result)):
  n -= result[i]
        
print(n)



# a=(input().split('-'))

# result = []
# # ['50', '50', '50+50']
# plus = 0
# for i in (a):
#   # find()
#   if i.find('+') != -1:
#     b = (i.split('+'))  # ['50', '50']
#     for j in b:
#       plus += int(j)
#     result.append(plus)
#   else:
#     result.append(int(i))
# n = result[0]
# for i in range(1, len(result)):
#   n -= result[i]
        
# print(n)