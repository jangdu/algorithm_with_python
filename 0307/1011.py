# # k - 1, k, k + 1
# # first
# 총이동거리-1    이동거리    공간이동을하는횟수
# 1               0           1
# 2               1           2  
# 3               11          3
# 4               12          3
# 5               121         4
# 6               122         4
# 7               1221        5
# 8               1222        5
# 9               1232        5
# 10              12321       6
# 11              12322       6
# 12              12332       6
# 13              123321      7
# 14              

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    d = y - x
    count = 0
    move = 1  # 이동가능거리
    sum = 0  # 이동한 거리의 합
    while sum < d :
        count += 1
        sum += move
        if count % 2 == 0:
            move += 1
    print(count)