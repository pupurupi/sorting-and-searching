import math

def jump_search(arr, target):
    # Returns: int: индекс элемента в массиве или -1 если не найден

    n = len(arr)
    if n == 0:
        return -1
    # Определяем размер прыжка (оптимально √n)
    step = int(math.sqrt(n))
    
    # Находим блок, где может находиться элемент
    prev = 0
    current = step
    
    # Прыгаем вперед, пока не найдем блок с возможным target
    while current < n and arr[current] < target:
        prev = current
        current += step
        # Если вышли за границы, устанавливаем верхнюю границу как n-1
        if current >= n:
            current = n
    
    # Линейный поиск в найденном блоке
    for i in range(prev, current):
        if arr[i] == target:
            return i
    
    return -1

# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    target_value = 15
    
    print(f"Массив: {sorted_array}")
    print(f"Ищем: {target_value}")
    
    result = jump_search(sorted_array, target_value)
    
    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")