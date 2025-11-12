def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr
    
    # 1. Определяем диапазон значений и количество корзин
    min_val = min(arr)
    max_val = max(arr)
    
    # Вычисляем количество корзин
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for i in range(bucket_count)]
    
    # 2. Распределяем элементы по корзинам
    for num in arr:
        # Вычисляем индекс корзины для текущего элемента
        bucket_index = (num - min_val) // bucket_size
        buckets[bucket_index].append(num)
    
    # 3. Сортируем каждую корзину индивидуально
    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])  # Используем сортировку вставками
    
    # 4. Объединяем корзины в порядке возрастания
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr


def insertion_sort(arr):
    # Вспомогательная функция - сортировка вставками
    # Используется для сортировки отдельных корзин

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Примеры использования и тестирование
if __name__ == "__main__":
    test_data2 = [29, 25, 3, 49, 9, 37, 21, 43]
    print("\nИсходный массив:", test_data2)
    sorted2 = bucket_sort(test_data2, bucket_size=10)
    print("Отсортированный массив:", sorted2)
    
    