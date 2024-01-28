import heapq

def heap_sort(iterable, descending=False):
    sign = -1 if descending else 1
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    return [sign * heapq.heappop(h) for _ in range(len(h))]

def calculate_min_cost_to_connect_cables(cable_lengths):
    # Використовуємо heap sort для сортування довжин кабелів у порядку зростання
    sorted_cables = heap_sort(cable_lengths)
    
    total_cost = 0
    while len(sorted_cables) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(sorted_cables)
        second = heapq.heappop(sorted_cables)

        # Об'єднуємо їх і додаємо витрати
        combined_length = first + second
        total_cost += combined_length

        # Додаємо новоутворений кабель назад у купу
        heapq.heappush(sorted_cables, combined_length)

    return total_cost

# Приклад використання функції
cable_lengths = [12, 11, 13, 5, 6, 7]
min_cost = calculate_min_cost_to_connect_cables(cable_lengths)
print(f"Мінімум загальних витрат - {min_cost}")

