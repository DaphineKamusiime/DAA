##binary search for  an unsorted array
def binary_search(array,search_value):
    
    beginning=0
    
    end=len(array)-1
    
    n=len(array)
        
    for i in range(len(array)):
            
        for j in range(len(array)-i-1):
                
            if array[j]>array[j+1]:
                    
                array[j],array[j+1]=array[j+1],array[j]
                    
                print(array)##printing sorted array
                    
    while beginning<=end:
                    mid=int((beginning+end)//2)
                    
                    if search_value==array[mid]:
                        return mid
                    
                    elif search_value<array[mid]:
                        end=mid-1
                        
                    else:

                        beginning=mid+1 
                                 
test_list=[4,1,2,3]

search_value1=4

print(binary_search(test_list,search_value1))

##bubble sort
def bubble_sortt(list1):

    count = 0
    v=len(list1)
    for i in range (v):
        swapped=False
        for j in range ((v-i)-1):#because after every iteration the last values will be at the end
            if list1[j]> list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1 [j+1]=temp
                swapped=True
        if not swapped :
            break
    
    return list1
list1=[19,27,23,10,6,11]

print(bubble_sortt(list1))

