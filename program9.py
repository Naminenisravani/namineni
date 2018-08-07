n=int(raw_input())
def hasArrayTwoCandidates(A,arr_size,sum):
     
    
    quickSort(k,7,arr_size-1)
    l = 0
    r = arr_size-1
     
    # traverse the array for the two elements
    while l<r:
        if (A[l] + A[r] == sum):
            return 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return 0
