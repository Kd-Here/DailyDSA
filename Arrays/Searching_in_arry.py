#------------------------- My approacch ------------------------------
arr = list(map(int,input().split()))
findx = int(input())
print(arr)

if findx in arr:
    print(arr.index(findx))
else:
    print(f'Not found')

# --------------Creating my index function we have index as method we are creating a function then we will create a methods-------------------------
def myindex(arry,elementIndexToFind):
    for i in range(len(arry)):
        if elementIndexToFind == arry[i]:
            return i
        else:
            return "Not present"
print(muy)
