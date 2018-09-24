##BUBBLE_SORT
array = [9, 7, 8, 1, 3, 6, 5, 2, 4]

def bubble_sort(array):
    corrected = True
    while(corrected):
        corrected = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                corrected = True
    return array
print(bubble_sort(array))