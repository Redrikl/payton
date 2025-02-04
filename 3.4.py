from collections import Counter

def main():
    n = int(input("Сколько строк вы хотите ввести? "))
    lines = []
    for i in range(n):
        line = input(f"Строка {i+1}: ")
        lines.append(line)

    # Объединяем все строки в один текст
    all_text = "".join(lines)
    total_chars = len(all_text)

    if total_chars == 0:
        print("Нет символов вообще — нельзя определить самый распространённый символ.")
        return

    # Считаем частоты всех символов в объединённом тексте
    counts = Counter(all_text)
    # Находим символ с максимальным числом вхождений
    most_common_char, max_count = max(counts.items(), key=lambda x: x[1])
    # Глобальная частота этого символа во всех строках
    global_freq = max_count / total_chars

    def squared_deviation(line: str) -> float:
        """
        Возвращает (freq_in_line - global_freq)^2,
        где freq_in_line — частота самого распространённого (глобально) символа в данной строке.
        """
        length = len(line)
        if length == 0:
            # Если строка пустая, частота этого символа 0
            return (0 - global_freq) ** 2
        freq_in_line = line.count(most_common_char) / length
        return (freq_in_line - global_freq) ** 2

    # Сортируем строки по возрастанию квадратичного отклонения
    sorted_lines = sorted(lines, key=squared_deviation)

    print("\nСамый распространённый символ в совокупности строк:", repr(most_common_char))
    print(f"Его глобальная частота: {global_freq:.6f}\n")

    print("Строки в порядке увеличения квадратичного отклонения:")
    for line in sorted_lines:
        dev = squared_deviation(line)
        freq_in_line = (line.count(most_common_char) / len(line)) if len(line) else 0
        print(f"{line!r} -> отклонение={dev:.6f}, freq_in_line={freq_in_line:.6f}")

if __name__ == "__main__":
    main()
# Hello, world!
# AAA AAA AAA
# No repeated characters
# drgrdgrg grdrg