def most_frequent_letter_and_its_freq(line: str, freq_map: dict[str, float]) -> tuple[str, float]:
    """
    Ищет в строке line наиболее часто встречающуюся букву (из freq_map),
    возвращает кортеж (буква, относительная_частота_в_строке).
    
    Если в строке нет ни одной подходящей буквы, возвращает ('', 0.0).
    """
    # Переведём в нижний регистр, чтобы не путать с заглавными
    lower_line = line.lower()
    
    # Подсчитаем частоты только «учитываемых» букв
    counts = {}
    total_letters = 0
    
    for ch in lower_line:
        if ch in freq_map:  # Если символ есть в словаре частот
            counts[ch] = counts.get(ch, 0) + 1
            total_letters += 1

    if total_letters == 0:
        # Ни одной буквы из freq_map не нашлось
        return ('', 0.0)

    # Находим букву, которую встречаем чаще всего в строке
    most_freq_char = max(counts, key=counts.get)
    # Рассчитываем относительную частоту этой буквы в строке
    freq_in_line = counts[most_freq_char] / total_letters
    
    return (most_freq_char, freq_in_line)

def squared_deviation(line: str, freq_map: dict[str, float]) -> float:
    """
    Вычисляет квадратичное отклонение частоты самой часто
    встречающейся в line буквы (из freq_map) от её «эталонной» частоты:
        (freq_in_line - freq_etalon)**2.
    
    Если в строке нет букв из freq_map, возвращает 0.
    """
    ch, freq_in_line = most_frequent_letter_and_its_freq(line, freq_map)
    if ch == '':
        # Нет ни одной подходящей буквы
        return 0.0
    
    freq_etalon = freq_map[ch]
    return (freq_in_line - freq_etalon) ** 2

def main():
    # Полный список букв русского алфавита с их приблизительными частотами
    # (в сумме может не давать точно 1.0, это нормально).
    RUS_FREQS = {
        'а': 0.0801,
        'б': 0.0145,
        'в': 0.0454,
        'г': 0.0170,
        'д': 0.0298,
        'е': 0.0845,
        'ё': 0.0001,  # встречается реже остальных
        'ж': 0.0094,
        'з': 0.0165,
        'и': 0.0735,
        'й': 0.0104,
        'к': 0.0349,
        'л': 0.0440,
        'м': 0.0323,
        'н': 0.0670,
        'о': 0.1097,
        'п': 0.0281,
        'р': 0.0473,
        'с': 0.0547,
        'т': 0.0632,
        'у': 0.0262,
        'ф': 0.0026,
        'х': 0.0097,
        'ц': 0.0048,
        'ч': 0.0121,
        'ш': 0.0073,
        'щ': 0.0036,
        'ъ': 0.0004,
        'ы': 0.0190,
        'ь': 0.0174,
        'э': 0.0032,
        'ю': 0.0064,
        'я': 0.0201
    }

    n = int(input("Сколько строк вы хотите ввести? "))
    lines = []
    for i in range(n):
        line = input(f"Строка {i+1}: ")
        lines.append(line)

    # Сортируем строки по возрастанию квадратичного отклонения
    sorted_lines = sorted(lines, key=lambda x: squared_deviation(x, RUS_FREQS))

    print("\nСтроки в порядке возрастания квадратичного отклонения:")
    for line in sorted_lines:
        dev = squared_deviation(line, RUS_FREQS)
        print(f"{line!r} -> отклонение={dev:.6f}")

if __name__ == "__main__":
    main()
# Загадочная погода: то снег, то дождь…
# Привет, как у вас дела сегодня?
# 12345 !@#$$%^
# ОООООО, какие тут интересные буквы!