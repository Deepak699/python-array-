import numpy as np
d = 69
arr = np.array([40 ,13, 27, 87, 95, 40, 96, 71, 35, 79, 68, 2 ,98, 3, 18, 93, 53, 57, 2, 81, 87 ,42, 66, 90, 45, 20, 41, 30 ,32, 18, 98 ,72, 82, 76 ,10, 28, 68 ,57, 98, 54, 87 ,66, 7, 84 ,20, 25, 29 ,72 ,33, 30 ,4 ,20, 71, 69, 9, 16, 41, 50, 97 ,24, 19, 46 ,47, 52, 22 ,56, 80, 89, 65, 29, 42, 51, 94 ,1, 35, 65 ,25
])
n = np.product(arr.shape)
temp = np.empty([2])
temp = arr[0:d]
arrcomb = np.array([d])
i = 0
def rotate(arr,d,n):
    for  x in range(d):
        arr = np.delete(arr,i)
        arrcomb =np.concatenate((arr,temp))
        print(arrcomb)
        return arrcomb


rotate(arr,d,n)