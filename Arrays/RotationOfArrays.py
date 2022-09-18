# Taking inputs
# InputArry = input().split()
# Rotations = int(input())


arry = list(map(int,input().split()))


for i in range(int(input())):
    l2 = []
    for j in range(len(arry)):
        if j!= 0:
            l2.append(arry[j])
    l2.append(arry[0])
    print(l2)
    arry = l2