arr = [1,-2,-3,4,-8,8,-9,-10,9,-10]

# # def Compare(x,y):
# #     if x[y] < 9:
# #         print(y)
# #         return 
# #     else:
# #         Compare(x,(y-1))

# # Compare(a,-1)

# # Play with position of even and odd

for i in range(len(arr)):
    if i%2 == 0: #Even
        if arr[i]<0:    #Even with -ve
            for j in arr[i:]:
                if j >0:
                    c = arr.pop(i)
                    arr.insert(i+1,c)
                    #remove element at the index
                    break

    else: #Odd
        if arr[i] > 0:  #Odd with +ve
            for j in arr[i:]:
                if j <0:
                    c = arr.pop(i)
                    arr.insert(i+1,c)
                    break
print(arr)

# # 
