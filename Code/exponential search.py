def exponential_search(arr, target):
    # Returns:int: индекс элемента в массиве или -1 если не найден
    n = len(arr)
    
    if n == 0:
        return -1
    
    # Проверяем первый элемент
    if arr[0] == target:
        return 0
    
    # Экспоненциально увеличиваем диапазон поиска
    i = 1
    while i < n and arr[i] <= target:
        if arr[i] == target:
            return i
        i *= 2
    
    # Выполняем бинарный поиск в найденном диапазоне
    left = i // 2  # Начало диапазона
    right = min(i, n - 1)  # Конец диапазона (не выходим за границы)
    
    return binary_search(arr, target, left, right)


def binary_search(arr, target, left, right):
    # Вспомогательная функция бинарного поиска
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    target_value = 15
    
    print(f"Массив: {sorted_array}")
    print(f"Ищем: {target_value}")
    
    result = exponential_search(sorted_array, target_value)
    
    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")