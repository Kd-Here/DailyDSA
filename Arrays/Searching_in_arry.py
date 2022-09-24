#------------------------- My approacch ------------------------------
from operator import index


arr = list(map(int,input().split()))
findx = int(input())
print(arr)

if findx in arr:
    print(arr.index(findx))
else:
    print(f'Not found')