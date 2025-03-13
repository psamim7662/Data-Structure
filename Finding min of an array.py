def find_min(arr):
    if len(arr)==0:
        return None 
    minimum_value=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<minimum_value:
            minimum_value=arr[i]
    return minimum_value
arr=[1,4,5,6,8,456]
print("The minimum value is:",find_min(arr))