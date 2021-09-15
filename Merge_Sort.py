import numpy as np
from time import time
from numpy.core.defchararray import array

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
   
    L = []
    R = []
 
    for i in range(0, n1):
        L.append(A[p+i])
        
    for j in range(0, n2):
        R.append(A[q+j+1])
 
    
    i = 0     
    j = 0     
    k = p     
 
    while i in range(len(L)) and j in range(len(R)):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k+=1
    
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

 
def mergeSort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)
 


# make random arrays
magnitude = 7
arrays = []
for i in range(1,magnitude):
    n = 10**i
    arrays.append(np.random.rand(n))
# sort and time the arrays
times = []
for array in arrays:
    n = len(array)
    startTime = time()
    mergeSort(array, 0, n-1)
    endTime = time()
    times.append(endTime - startTime)

for t in range(len(times)):
    print("when n is " + str(10**(t+1)) + " the time to sort is " + str(times[t]))

# the following is in seconds
# when n is 10 the time to sort is 8.463859558105469e-05
# when n is 100 the time to sort is 0.0008516311645507812
# when n is 1000 the time to sort is 0.014829397201538086
# when n is 10000 the time to sort is 0.15565156936645508
# when n is 100000 the time to sort is 1.961111068725586
# when n is 1000000 the time to sort is 23.71603536605835