def bead_sort(arr):
    if not arr:
        return arr

    # Находим максимальное значение для определения размера сетки
    max_val = max(arr)
    n = len(arr)
    
    # Создаем "абак" - матрицу бусин
    # abacus[i][j] = 1 означает, что на позиции (i,j) есть бусина
    abacus = [[0] * max_val for i in range(n)]
    
    # 1. Размещаем бусины на абаке
    for i in range(n):
        for j in range(arr[i]):
            abacus[i][j] = 1
    
    # 2. Даем бусинам "упасть" под действием гравитации
    for j in range(max_val):
        # Считаем количество бусин в текущем столбце
        bead_count = sum(abacus[i][j] for i in range(n))
        
        # "Сбрасываем" все бусины в столбце
        for i in range(n):
            abacus[i][j] = 0
        
        # Размещаем бусины внизу столбца (гравитация)
        for i in range(n - bead_count, n):
            abacus[i][j] = 1

    # 3. Считываем результат (снизу вверх)
    result = []
    for i in range(n):
        # Считаем количество бусин в строке
        bead_count = sum(abacus[i])
        result.append(bead_count)
    
    # Возвращаем в порядке убывания (так работает алгоритм)
    return result

# Примеры использования и тестирование
if __name__ == "__main__":
    
    # Тест 1:
    test_data1 = [3, 1, 4, 2]
    print(f"Тест 1: {test_data1}")
    sorted1 = bead_sort(test_data1.copy())
    print(f"Результат: {sorted1}\n")
    
    # Тест 2: 
    test_data2 = [7, 2, 9, 4, 6]
    print(f"Тест 2: {test_data2}")
    sorted2 = bead_sort(test_data2)
    print(f"Результат: {sorted2}")
    

