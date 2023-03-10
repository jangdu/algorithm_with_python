import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, x)
        
    else:
        print(heapq.heappop(heap) if len(heap) != 0 else 0)

#heapq.heappush(heap, i * -1)