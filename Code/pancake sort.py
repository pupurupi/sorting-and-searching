def pancake_sort(arr):
   
    # Создаем копию массива, чтобы не изменять оригинал
    arr = arr.copy()
    n = len(arr)
    
    for curr_size in range(n, 1, -1):
        # 1. Находим индекс максимального элемента в неотсортированной части
        max_index = find_max_index(arr, curr_size)
        
        # Если максимальный элемент уже на своем месте, пропускаем перевороты
        if max_index != curr_size - 1:
            # 2. Переворачиваем до максимального элемента, чтобы он стал первым
            if max_index != 0:
                flip(arr, max_index)
            
            # 3. Переворачиваем весь подмассив, чтобы максимальный элемент 
            # оказался в конце неотсортированной части
            flip(arr, curr_size - 1)
    return arr


def flip(arr, k):
        # arr: список элементов
        # k: индекс, до которого переворачиваем (включительно)

    left = 0
    right = k
    
    while left < right:
        # Меняем элементы местами
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def find_max_index(arr, n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

# Пример тестированиz
if __name__ == "__main__":
    print("=== Блинная сортировка ===")
    
    test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"\nТест 4:")
    print(f"Исходный массив: {test_data}")
    sortedd = pancake_sort(test_data)
    print(f"Отсортированный: {sortedd}")