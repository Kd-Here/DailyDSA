arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(arr)
for i in range(len(arr)):
    for j in arr:                 # this is same logic as `in` in python where in simply creates a loop
        if arr[i] == j:
            print(arr[i])
            break

    else:
        print(-1)


######################
#Finding efficient way
######################
