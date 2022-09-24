# Tommorws task is to find source code of python various built in function & methods.





#------------------------- My approacch ------------------------------
arr = list(map(int,input().split()))
findx = int(input())
print(arr)

if findx in arr:
    print(arr.index(findx))
else:
    print(f'Not found')























# --------------Creating my index function we have index as method we are creating a function then we will create a methods-------------------------
# def myindex(arry,elementIndexToFind):
#     i = 0; b =  len(arry) 
#     while(i < b):
#         if elementIndexToFind == arry[i]:
#             return i+1
#         i += 1
#     else:
#         return "Not present"

# print(myindex(a,9))
# a = [1,2,3,4,5,6,7]




# ___________________________________Created MyIndex class who has method of Findindex_____________________________
# class MyIndex:
#     def __init__(self,arry,elementIndexToFind):
#         self.Kd_aryy = arry
#         self.ElementIndexToFind = elementIndexToFind
    
#     def Findindex(self,ass):
#         for i in range(len(self.Kd_aryy)):
#             if self.Kd_aryy[i] == ass:
#                 print(i+1)
#                 break
#         else:
#             print("No Found")


# givenArry = list(map(int,input("Give me arry:- ").split()))
# Getindexof = int(input("Give element whose index you want:- "))

# a = MyIndex(givenArry,8)
# a.Findindex(Getindexof)
