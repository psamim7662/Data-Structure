def insert_at_beginning(array,array_max,ub,n,ele):
    if ub==array_max-1:
        print("Insertion is not possble")
        return ub,n
    for k in range(ub,-1,-1):
        array[k+1]=array[k]
    array[0]=ele
    ub +=1
    n +=1
    return ub,n
array_max=4
array=[10,20,30,None]
ub=2
n=3
ele=75

ub,n=insert_at_beginning(array,array_max,ub,n,ele)
print("Elemnts after inserting:",array[:n])
        