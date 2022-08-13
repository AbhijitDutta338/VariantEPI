'''
Problem: to find entry equal to index (Array is sorted but may contain duplicates)
'''

'''
If elements are not distinct, we cannot conclude which side the has required element is on. 
We know if A[5] = 3, A[4] could not be required element because arr[4] must be 
less than or equal to arr[5] as the array is Sorted i.e., arr[4]<=3 but should be 4 for becoming required element
So, the general pattern of our search would be: 

    Left Side: hi = min(arr[mid], mid-1) #A[mid]>mid
    Right Side: lo = max(arr[mid], mid+1) #A[mid]<mid
'''
'''
Honestly, just do a linear search here as the below algorithm also has O(n) time complexity.
solution taken from - https://www.geeksforgeeks.org/find-fixed-point-value-equal-index-given-array-duplicates-allowed/
'''
def magicIndex(arr, start, end):
    if (start > end): # If No Magic Index return -1
        return -1
    midIndex = int((start + end) / 2)
    midValue = arr[midIndex]
    
    if (midIndex == midValue): # Magic Index Found, return it.
        return midIndex
    
    left = magicIndex(arr, start, min(midValue, midIndex - 1)) # Search on Left side
    
    if (left >= 0): # If Found on left side, return.
        return left
    
    return magicIndex(arr, max(midValue, midIndex + 1), end) # Return ans from right side.
 
# Driver program
if __name__ == '__main__':
    arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    n = len(arr)
    print(magicIndex(arr, 0, n - 1))
