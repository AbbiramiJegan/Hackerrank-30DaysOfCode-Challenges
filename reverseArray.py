def reverseString(arr):
    reverseArray = arr[::-1]
    for i in range(len(reverseArray)):
        print(reverseArray[i], end=' ')
    

arr = [1, 2, 3, 4]
reverseString(arr)