def sort(array):
    less = []
    equal = []
    greater = []
 
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else: # if x > pivot
                greater.append(x)
        return sort(less) + equal + sort(greater)
    
    else:  
        return array
    
array=[12,4,5,6,7,3,1,15]
print(sort(array))