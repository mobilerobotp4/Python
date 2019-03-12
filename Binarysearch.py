#Binary search using recursion
def searchR(arr,key):
    return healper(arr,key,0,len(arr)-1)

def healper(arr,key,left,right):
    if left>right:
        return -1
    mid=(left+right)//2
    if key==arr[mid]: #Base Condition
        return mid
    else:
        if key>arr[mid]:
            return healper(arr,key,mid+1,right)
        else:
            return healper(arr,key,left,mid-1)



print(searchR([1,2,5,8,9],8))
