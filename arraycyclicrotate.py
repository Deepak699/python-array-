#User function Template for python3\
arr = [9, 8, 7, 6, 4, 2, 1, 3]
n = 8
temp = []
def rotate( arr, n):
    for i in arr:
        if i == n:
         temp = arr[n-1]
         arr.remove(n)
         arr.insert(0,temp)
         print(arr)

rotate(arr,n)

