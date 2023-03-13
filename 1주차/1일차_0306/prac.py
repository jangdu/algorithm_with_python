for _ in range(int(input())):
    a, b = map(int, input().split())
    x = 1
    if a == b:
        x = a
    elif a > b:
        if b == 1:
            x = b
            break
        else:
            for i in range(a, 0, -1):
                if a % i == 0 and b % i == 0:
                    x = i
    else:
        if b == 1:
                x = b
                break
        else:
            for i in range(b, 0, -1):
                if a % i == 0 and b % i == 0:
                    x = i
    
    print(a*b/x)