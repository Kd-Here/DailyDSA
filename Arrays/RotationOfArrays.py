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
    
    
    
#   Fastest way is to remove term till rotate number and put them at last
# Here first and second number are removed boz of rotate = 2 and put in back 
# Just remember we used list addition
l1 = [1,2,3,4,5]

def ArrayRotate(a,b):
    l2 = []
    l2 = l1[(rotate):]+l1[0:(rotate)]
    return l2
rotate = int(input())
ArrayRotate(l1,rotate)

