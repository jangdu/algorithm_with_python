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
T = int(input())
for i in range(T):
    s, d = map(int, input().split())
    d -= s
    n = 0
    count = 0
    temp = d + 1 if d % 2 != 0 else d

    for i in range(temp, 0, -1):
        if temp % i == 0:
            if temp == i:
                continue
            n = temp / i
            if i - n <= 1:
                break
    
    if d >= n ** 2 - (n - 1) and d <= n ** 2:
        count = n * 2 - 1
    else:
        count = n * 2

    print(count)