# We are finding element find in arry l1 



# This is brute force or basic way of creating 
l1 = list(map(int,input().split()))
find = int(input())

if find in l1:
  print(l1.index(find))
else:
  print("Not Found")
  
  
  
# Now we are learning binary searching
# Since our o/p want time complexity to be bigO(logn)


