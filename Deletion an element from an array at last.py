def delete_at_last(arr):
    if len(arr)==0:
        print("Not a valid index or out of range ")
        return arr
    arr.pop()
    return arr
arr=[1,3,4,5]
print("Array after delete last element:",delete_at_last(arr.copy()))