
def quicksort(array):
        less = []
        equal = []
        greater = []
        if len(array)>1:
            pivot = array[int(len(array)/2)]
            for i in range(len(array)):
                if array[i] < pivot:
                    less.append(array[i])                  
                if array[i] == pivot:
                    equal.append(array[i])
                if array[i] > pivot:
                    greater.append(array[i])
            less = quicksort(less)
            greater = quicksort(greater)
            array = less+equal+greater
        return array        
if __name__ == '__main__':    
    array = [3,4,2,6,10,23,1,5,34,235,43,2345,24,23,23,541,123,24,354,56,34,23,122,32,12,10,2,3,4,5,6,32,12,12,332,1,2,5]
    array = quicksort(array)
    print(array)