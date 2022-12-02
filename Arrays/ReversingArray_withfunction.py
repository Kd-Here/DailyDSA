A = [1, 2, 3, 4, 5, 6,7,8,9,10]


def Reveseded(A):
    B = len(A)
    while B>0:
        print(A[B-1])
        B -= 1
Reveseded(A)





# print("Reversed array")
# Ans = A[::-1]
# print(Ans)


########################
# Using recursive function
########################

def A1(A,index):
    if index>=0:
        C = index-1
        print(A[index])
        A1(A,C)

print("Hi")
A1(A,9)