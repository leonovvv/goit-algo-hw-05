def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])  # Знайшли точний збіг
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо точного збігу немає, повертаємо кількість ітерацій і верхню межу
    return (iterations, upper_bound)

# Тестуємо двійковий пошук:
sorted_array = [0.1, 0.5, 1.2, 2.3, 3.5, 5.8, 7.9, 10.5]
target = 4.0

iterations, upper_bound = binary_search(sorted_array, target)
print(f"Ітерацій: {iterations}, Верхня межа: {upper_bound}")
