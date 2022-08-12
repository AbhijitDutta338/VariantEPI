'''
Problem: Write a program which takes a sorted array A of integers, and an integer k, 
and returns the interval enclosing k, i.e, the pair of integers L and U such that 
L is the first occurance of k in A and U is the last occurance of k in A.
If k does not appear in A, return [-1,-1]. 
'''

from unittest import result


def search(A: list[int], k: int, flag: bool)-> int:
    result = -1
    lo, hi = 0, len(A)-1
    while(lo<=hi):
        mid = lo + (hi-lo)//2
        if(A[mid]==k):
            result=mid
            if(flag):
                hi=mid-1
            else:
                lo=mid+1
        elif(A[mid]>k):
            hi=mid-1
        else:
            lo=mid+1
    return result
         

def solution(A: list[int], k: int)-> list[int]:
    result=list()
    #Fetch the first occurance
    result.append(search(A,k,True))
    #Fetch the last occurance
    result.append(search(A,k,False))
    return result

if __name__=='__main__':
    A=[1, 2, 2, 4, 4, 4, 7, 11, 11, 13]
    # [0| 1| 2| 3| 4| 5| 6| 7 |  8|  9]
    k=int(input())
    print("Input -> A={}, k={}".format(A,k))
    print(solution(A,k))
