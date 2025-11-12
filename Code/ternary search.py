def ternary_search(arr, target):
    # Returns:int: индекс элемента в массиве или -1 если не найден
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Делим диапазон на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"Диапазон [{left}, {right}]: mid1={mid1}, mid2={mid2}")
        
        # Проверяем граничные точки
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Определяем в какой трети продолжать поиск
        if target < arr[mid1]:
            # Искомый элемент в первой трети
            right = mid1 - 1
        elif target > arr[mid2]:
            # Искомый элемент в третьей трети
            left = mid2 + 1
        else:
            # Искомый элемент во второй трети
            left = mid1 + 1
            right = mid2 - 1
    
    return -1


# Рекурсивная версия тернарного поиска
def ternary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    if target < arr[mid1]:
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)


# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    target_value = 15
    
    print(f"Массив: {sorted_array}")
    print(f"Ищем: {target_value}")
    print("\nИтеративная версия:")
    
    result = ternary_search(sorted_array, target_value)
    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")
    
    print("\nРекурсивная версия:")
    result_recursive = ternary_search_recursive(sorted_array, target_value, 0, len(sorted_array) - 1)
    if result_recursive != -1:
        print(f"Элемент найден на позиции: {result_recursive}")
    else:
        print("Элемент не найден")