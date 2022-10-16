# # import math

# # class Points(object):
# #     def __init__(self, x, y, z):
# #         self.x = x
# #         self.y = y
# #         self.z = z

# #     def __sub__(self, no):
# #         x=self.a1 - no.a1
# #         y=self.a2 - no.a2
# #         z= self.a3-no.a3
# #         return x,y,z
# #         # return self.x - no.x, self.y - no.y, self.z-no.z

# #     def dot(self, no):
# #         x=self.a1*no.a1
# #         y=self.a2*no.a2
# #         z= self.a3*no.a3
# #         return x,y,z

# #     def cross(self, no):
        
# #     def absolute(self):
# #         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

# # if __name__ == '__main__':
# #     points = list()
# #     for i in range(4):
# #         a = list(map(float, input().split()))
# #         points.append(a)

# #     a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
# #     x = (b - a).cross(c - b)
# #     y = (c - b).cross(d - c)
# #     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

# #     print("%.2f" % math.degrees(angle))

# from re import X


# class Points():
#     def __init__(self, x, y, z):
#         self.a1 = x
#         self.a2 = y
#         self.a3 = z
    
    
#     def __sub__(self,no):
#         x=self.a1 - no.a1
#         y=self.a2 - no.a2
#         z= self.a3-no.a3
#         l = []
#         l.append(x)
#         l.append(y)
#         l.append(z)
#         return l
        
#     def printing(self,a1):
#         print("THe values are 2 different values furst is bcoz of self",self.a1)
#         print("THe values are 2 different values 2nd is user passed argument",a1)
    
#     def dot(self,no):
#         x=self.a1*no[0]
#         y=self.a2*no[1]
#         z= self.a3*no[2]
#         l = []
#         l.append(x)
#         l.append(y)
#         l.append(z)
#         return l
        

# points = list()
# for i in range(4):
#     a = list(map(float, input().split()))
#     points.append(a)
# print(points)
# print(*points[0])
# a, b,c,d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
# x = (b - a)
# y = (c-d)
# print(x)
# print(y)
# z = a.dot(y)
# print(z)




class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x=self.x - no.x
        y=self.y - no.y
        z= self.z-no.z
        c = Points(x,y,z) #creating a object of value for easy calculation
        return  c

   

if __name__ == '__main__':
    points = list()
    for i in range(2):
        a = list(map(float, input().split()))
        points.append(a)

    a, b = Points(*points[0]), Points(*points[1])
    print(a.x)
    print(b.y)
    print(type(a))
    x = (b - a)
    print(x.x,x.y,x.z)
