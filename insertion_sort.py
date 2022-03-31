def insertion_sort(list_1):
    '''

    :param list_1: initialize a parameter of a list in function
    :return: insertion sort in sorted order
    '''
    for i in range(1, len(list_1)):  # Outer loop to traverse through 1 to len(list1)
        temp = list_1[i]
        j = i - 1
        while j >= 0 and temp < list_1[j]:
            list_1[j + 1] = list_1[j]
            j -= 1
        list_1[j + 1] = temp
    return list_1


if __name__ == '__main__':
    list1 = [12, 4, 31, 3, 5, 1]
    print("Unsorted list is: ", list1)
    print("sorted list is : ", insertion_sort(list))