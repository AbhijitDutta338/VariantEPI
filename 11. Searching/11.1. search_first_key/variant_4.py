#Problem: Write a program which tests if p is a prefix of a string in an array of sorted strings

def isprefix(key: str, ele: str)-> int:
    for i in range(len(key)):
        if(key[i]==ele[i]):
            continue
        else:
            if(key[i]>ele[i]): 
                return 1 #CASE of key>mid -> lo = mid+1
            else:
                return -1 #CASE of key<mid -> hi = mid-1
    return 0 #CASE of equality, prefix found


def solution(A: list[str], k: str)-> bool:
    lo, hi = 0, len(A)-1
    while(lo<=hi):
        mid = lo +(hi-lo)//2
        if(isprefix(k,A[mid])==0):
            return True
        elif(isprefix(k,A[mid])==1):
            lo=mid+1
        elif(isprefix(k,A[mid])==-1):
            hi=mid-1
    return False

if __name__=='__main__':
    A=["aa","aba","american","australia","backbench","joyboy","millionaire","moneyflows","onepiece","zoro"]
    k=input()
    #print("Input -> A={}, k={}".format(A, k))
    print(solution(A,k))
