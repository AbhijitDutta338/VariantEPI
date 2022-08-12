'''
Problem: Let A be an unsorted array of n integers, with A[0]>=A[1] and A[n-2]<=A[n-1]. 
Call an index i a local minimum if A[i] is less than or equal to its neighbors 
How would you efficiently find a local minimum if one exists??
'''
'''
Solution methodology:
More clear constraint:-
1. Distinct integer array
2. Only one local minimum if exists 

Critical Idea- Given the above conditions,
local minima if exists lies in the array, 
    as A[0]>=A[1] && A[n-1]>=A[n-2]
if A[mid] is greater than A[mid-1]:
    then the local minima if exists lies in the left part as
    A[0]>=A[1] && A[mid]>A[mid-1]
if A[mid] is greater than A[mid+1]:
    then local minima if exists lies in the right part as
    A[mid]>A[mid+1] && A[n-1]>=A[n-2] 
'''
def solution(A: list[int])->int:
    lo, hi = 0, len(A)-1
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        print("lo={}, hi={}, mid={}".format(lo, hi, mid))
        if((mid==0 or A[mid-1]>=A[mid]) and (mid==len(A)-1 or A[mid]<=A[mid+1])):
            # case of finding local minima in the array or at the ends of array
            return mid
        elif(mid>0 and A[mid]>A[mid-1]):
            hi=mid-1
        else:
            lo=mid+1

    return -1


if __name__=='__main__':
    A=[500, 19, 109, 108, 107]#, 143, 285, 286, 287, 401]
    # [ 0 |   1|   2|  3 |  4 |  5 |  6 |  7 |  8 |   9]
    print("Input -> A={}".format(A))
    print(solution(A))
