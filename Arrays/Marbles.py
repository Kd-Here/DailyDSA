arr = [1,-2,-3,4,-8,8,-9,-10,9,-10]

# # def Compare(x,y):
# #     if x[y] < 9:
# #         print(y)
# #         return 
# #     else:
# #         Compare(x,(y-1))

arr = [-9,-1,-4,-2,30,4,5,8]


arr = [-9,-1,-4,-2,30,4,5,8]

for i in range(len(arr)):
    if i%2 == 0: #Even
        if arr[i]<0:    #Even with -ve
            for j in range(len(arr[i:])):
                if arr[j] >0:
                    arr[j] = arr[j] + arr[i]
                    arr[i] = arr[j] - arr[i]
                    arr[j] = arr[j] - arr[i]
                    #remove element at the index
                    break

    else: #Odd
        if arr[i] > 0:  #Odd with +ve
            for j in range(len(arr[i:])):
                if arr[j] <0:
                    arr[j] = arr[j] + arr[i]
                    arr[i] = arr[j] - arr[i]
                    arr[j] = arr[j] - arr[i]
                    break
print(arr)
# # 


