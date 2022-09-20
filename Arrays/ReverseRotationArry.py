class ReverseArry:
    # def __init__(self,first,second):
    #     self.arry = first
    #     #This is arry which we want to change
    #     self.rotate = second
    #     # self.rotate is number to break arry
     
    def rotatedArray(self):
        a = (self.arry)
        b = (self.rotate)
        l2 = list(a[b:]+a[0:b])
        return f"The reverse array is {l2}"


arry = list(map(int,input().split()))
print("Your input array is",arry)
Rotation = int(input())
obj = ReverseArry(arry,Rotation)
print(obj.rotatedArray())

