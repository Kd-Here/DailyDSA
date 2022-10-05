array = [1,2,3, 4, 5, 6, 7, 8, 9]
x = int(input())
h = len(array)-1

def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while (low <= high):
        mid = (low + high)//2

        if array[mid] == x:
            return f"{mid}"

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return f"Not found"


result = binarySearch(array, x, 0, h)
print(result)


# #########################
# Binary Search with Recursive method:-
# #########################

