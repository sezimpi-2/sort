def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(element, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid - 1
        else:
            return mid
    return -1

unsorted_list = [98, 23, 56, 72, 11, 34, 87, 45, 1, 77, 65, 88, 33, 99, 10, 25, 42, 59, 20, 76, 51, 85, 7, 94, 62, 14, 69, 38, 90, 50, 83, 31, 97, 84, 22, 9, 2, 74, 6, 96, 39, 60, 19, 91, 49, 78, 17, 73, 61, 5, 30, 57, 36, 95, 44, 21, 26, 89, 8, 70, 12, 71, 27, 41, 80, 64, 35, 18, 66, 46, 92, 43, 75, 13, 63, 58, 55, 28, 16, 86, 68, 3, 15, 82, 48, 40, 54, 79, 52, 24, 67, 53, 4, 81, 32, 37, 93, 47]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

element_to_find = 47
index = binary_search(element_to_find, sorted_list)
if index != -1:
    print(f"Элемент {element_to_find} найден в позиции {index}.")
else:
    print(f"Элемент {element_to_find} не найден в списке.")
