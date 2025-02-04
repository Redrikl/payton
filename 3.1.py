def average_ascii_value(s: str) -> float:
    """
    Возвращает среднее значение ASCII-кода символов в строке s.
    Для пустой строки условно вернёт 0.
    """
    return sum(ord(ch) for ch in s) / len(s) if len(s) > 0 else 0

def main():
    # Считываем количество строк
    n = int(input("Сколько строк вы хотите ввести? "))

    lines = []
    for i in range(n):
        line = input(f"Строка {i+1}: ")
        lines.append(line)

    # Сортируем строки по возрастанию среднего веса (ASCII) символов
    sorted_lines = sorted(lines, key=average_ascii_value)

    print("\nСтроки в порядке увеличения среднего ASCII-кода:")
    for line in sorted_lines:
        print(line)

if __name__ == "__main__":
    main()
