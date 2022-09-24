# Read dunder methods from real python

class ReverseArry:
    def __init__(self,first,second):
        self.arry = first
        #This is arry which we want to change
        self.rotate = second
        # self.rotate is number to break arry

    def __index__(self):
            return (self)
            # A dunder means double underscore which is use to overrides the method operations here we are overiding index when obj.rotate index is calling it will return the index value of it.

    def rotatedArray(self):
        # Here we used object property for indexing but earlier given an error but resolved bcoz of dunder method which is above index
        l2 = list(self.arry[self.rotate:]+self.arry[0:self.rotate])
        return f"The reverse array is {l2}"


        # This is normal method of class object!
        # a = (self.arry)
        # b = (self.rotate)
        # l2 = list(a[b:]+a[0:b])


        
        

arry = list(map(int,input().split()))
print("Your input array is",arry)
Rotation = int(input())
obj = ReverseArry(arry,Rotation)
print(obj.rotatedArray())
print(obj.rotate)
