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

### sum(stack)
t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    rs = r1 + r2
    rm = abs(r1 - r2)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rs or d == rm:
            print(1)
        elif d < rs and d > rm:
            print(2)
        else:
            print(0)