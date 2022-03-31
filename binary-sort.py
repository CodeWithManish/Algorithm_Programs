def binary_search(arr, item):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == item:
            return True
        if item < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    word = ["banana", "mango", "grape", "apple", "cherry", "Orange"]
    name = input("enter name : ")
    result = binary_search(word, name)
    if not result:
        print("Element not found")
    else:
        print(f"Element found")