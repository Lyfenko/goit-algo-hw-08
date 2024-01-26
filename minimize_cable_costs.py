import heapq


def minimize_cable_costs(cable_lengths):
    heapq.heapify(cable_lengths)

    total_costs = 0

    while len(cable_lengths) > 1:
        first_cable = heapq.heappop(cable_lengths)
        second_cable = heapq.heappop(cable_lengths)
        current_costs = first_cable + second_cable

        # Додавання витрат за об'єднання до загальних витрат
        total_costs += current_costs

        # Додавання нового кабелю (результату об'єднання) до купи
        heapq.heappush(cable_lengths, current_costs)

    return total_costs


if __name__ == "__main__":
    try:
        user_input = input("Введіть довжини кабелів через пробіл: ")
        cable_lengths = list(map(int, user_input.split()))

        # Перевірка на парність кількості кабелів
        if len(cable_lengths) % 2 != 0:
            raise ValueError("Кількість кабелів повинна бути парною.")

        total_costs = minimize_cable_costs(cable_lengths)
        print(f"\nМінімальні загальні витрати для об'єднання кабелів: {total_costs}")

    except ValueError as e:
        print(f"Помилка: {e}. Будь ласка, введіть коректні дані.")
