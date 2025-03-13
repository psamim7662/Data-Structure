def find_max(arr):
    if len(arr)==0:
        return None
    maximum_value=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maximum_value:
            maximum_value=arr[i]
    return maximum_value
arr=[12,45,56]
print("The maximum value of this array is:",find_max(arr))