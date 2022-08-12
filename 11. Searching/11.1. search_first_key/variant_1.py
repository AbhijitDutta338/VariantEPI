#Problem- first occurance of element greater than key
def solution(A: list[int], k: int)-> int:
   result = -1
   lo, hi = 0, len(A)-1
   while(lo <= hi):
    mid = lo + (hi-lo)//2
    if(A[mid] < k):
        lo = mid+1
    elif(A[mid]==k):
        result=mid
        lo=mid+1 #for finding the last occurance of key k if k is present
    else:
        hi = mid-1
   if(result==-1):
    # if key is not present than the lo is always the first greater element than the key k  
    return lo 
   # if key is present result contains the last occurance position of k, returning the next position i.e, the first occurance of greater element
   return result+1 

if __name__=='__main__':
    #A=list(map(int, input().split()))
    A=[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    k=int(input())
    print("Input -> A={}, k={}".format(A,k))
    print(solution(A,k))
