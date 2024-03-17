def merge_sort(num_array):
    if len(num_array) <= 1:
        return num_array

    # splits the array's into two parts
    mid = len(num_array) // 2
    left_half = num_array[:mid]
    print(left_half)
    right_half = num_array[mid:]
    print(right_half)

    # starts to sort them
    left_half = merge_sort(left_half)
    print(left_half)
    right_half = merge_sort(right_half)
    print(right_half)
    # merging the array into a new sorted one
    sorted_array = merge(left_half, right_half)
    return sorted_array


def merge(left_half, right_half):
    merged = []
    left_index = 0
    right_index = 0

    # Starts to merge the two arrays together
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1

        else:
            merged.append(right_half[right_index])
            right_index += 1

    # adds the left side into the sorted array
    while left_index < len(left_half):
        merged.append(left_half[left_index])
        left_index += 1
        print("left merge /n", left_index)

    # adds the right side into the sorted array
    while right_index < len(right_half):
        merged.append(right_half[right_index])
        right_index += 1
        print("right merge /n", right_index)

    return merged


num_array = []
while(True):
    temp = int(input("enter a positive number enter a negative to sort: "))
    if (temp >= 0):
        num_array.append(temp)
    elif (temp < 0):
        break
    else:
        print("incorrect variable")
sorted_array = merge_sort(num_array)
print("Sorted array:", sorted_array)
