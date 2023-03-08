import sys
def get_dist_between_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

T = int(sys.stdin.readline())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    d = get_dist_between_points(x1, y1, x2, y2)
    rs = r1 + r2
    rm = abs(r1 - r2)

    if d == 0:
      if r1 == r2:
        print (-1)
      else:
        print(0)
    else:
      if d == rs or d == rm:
        print(1)
      elif d < rs and d > rm:
        print(2)
      else :
        print(0)       
