def vc_cv_difference(line: str) -> int:
    """
    Возвращает абсолютную разницу между количеством пар «гласная–согласная»
    и количеством пар «согласная–гласная» в строке.
    """
    # Гласные буквы русского алфавита (учитываем только нижний регистр для упрощения)
    vowels = set("аеёиоуыэюя")
    
    # Подготовим строку: в нижнем регистре + оставим только русские буквы
    # (Если нужно учитывать и другие символы, просто не фильтруйте)
    lower_line = line.lower()
    
    # Счётчики
    count_vc = 0  # гласная -> согласная
    count_cv = 0  # согласная -> гласная
    
    # Идём по паре соседних символов
    for i in range(len(lower_line) - 1):
        ch1 = lower_line[i]
        ch2 = lower_line[i+1]
        
        # Проверяем, являются ли оба символа буквами
        if ('а' <= ch1 <= 'я' or ch1 == 'ё') and ('а' <= ch2 <= 'я' or ch2 == 'ё'):
            is_vowel_1 = (ch1 in vowels)
            is_vowel_2 = (ch2 in vowels)
            
            if is_vowel_1 and not is_vowel_2:
                count_vc += 1  # гласная–согласная
            elif not is_vowel_1 and is_vowel_2:
                count_cv += 1  # согласная–гласная
    
    # Абсолютная разница
    return abs(count_vc - count_cv)

def main():
    n = int(input("Сколько строк вы хотите ввести? "))
    lines = []
    for i in range(n):
        line = input(f"Строка {i+1}: ")
        lines.append(line)

    # Сортируем строки по возрастанию разницы
    sorted_lines = sorted(lines, key=vc_cv_difference)
    
    print("\nСтроки в порядке увеличения разницы (|VC - CV|):")
    for line in sorted_lines:
        diff = vc_cv_difference(line)
        print(f"{line!r} -> разница={diff}")

if __name__ == "__main__":
    main()
#Привет
#Ка как 
#Ак ака
#Акаак