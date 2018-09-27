##BUBBLE_SORT
num_list = [9, 7, 8, 1, 3, 6, 5, 2, 4]

def bubble_sort(num_list):
    corrected = True
    while(corrected):
        corrected = False
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                corrected = True
    return num_list
print(bubble_sort(num_list))