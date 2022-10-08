a = [1,2,3,4,8,8,9,0,9,0]

def Compare(x,y):
    if x[y] < 9:
        print(y)
        return 
    else:
        Compare(x,(y-1))

Compare(a,-1)
