##BUBBLE_SORT
num_list = [9, 7, 8, 1, 3, 6, 5, 2, 4]

def bubble_sort(num_list):
    brakes = True
    while(brakes):
        brakes = False
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                brakes = True
    return num_list
print(bubble_sort(num_list))