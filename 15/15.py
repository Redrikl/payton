import csv
import re

def parse_time_spent(time_str):
    """
    Парсит строку времени вида:
      - "1 ч. 19 мин."
      - "18 мин. 40 сек."
      - "2 ч. 05 мин. 30 сек."
      - и т.п.
    Возвращает суммарное число секунд (int).
    Если ничего не найдено, возвращаем -1.
    """

    # Инициализируем часы/минуты/секунды нулями
    hours = 0
    minutes = 0
    seconds = 0

    # Ищем в строке 'X ч' или 'X ч.'
    match_h = re.search(r'(\d+)\s*ч', time_str)
    if match_h:
        hours = int(match_h.group(1))
    
    # Ищем 'X мин' или 'X мин.'
    match_m = re.search(r'(\d+)\s*мин', time_str)
    if match_m:
        minutes = int(match_m.group(1))
    
    # Ищем 'X сек' или 'X сек.'
    match_s = re.search(r'(\d+)\s*сек', time_str)
    if match_s:
        seconds = int(match_s.group(1))

    total_sec = hours * 3600 + minutes * 60 + seconds
    
    # Если совсем не нашли ни часов, ни минут, ни секунд → total_sec = 0
    # Можно считать, что формат неизвестен
    if total_sec == 0 and "ч" not in time_str and "мин" not in time_str and "сек" not in time_str:
        return -1
    
    return total_sec

def parse_score_1(score_str):
    """
    Столбцы вида 'B. 1 /1,00' содержат оценки '0,00'..'1,00' (запятая как десятичный разделитель).
    Возвращает float от 0.0 до 1.0.
    Если не удалось преобразовать, вернём -1.
    """
    try:
        # Уберём пробелы, заменим запятую на точку
        s = score_str.strip().replace(',', '.')
        # Пример: "0,00" -> "0.00"
        val = float(s)
        return val
    except:
        return -1

def main():
    csv_filename = "15_-_2.csv"

    # Лимит времени — 20 минут = 1200 секунд
    time_limit_sec = 1200

    # Откроем CSV. Укажем delimiter=',' и quotechar='"', поскольку поля в кавычках, разделены запятыми.
    with open(csv_filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"')
        
        filtered_rows = []

        for row in reader:
            # Проверяем, что участник реально закончил тест
            if row.get("Состояние", "") != "Завершено":
                continue
            
            # Парсим затраченное время
            spent_str = row.get("Затраченное время", "")
            spent_sec = parse_time_spent(spent_str)
            # Проверим, уложился ли в лимит
            if spent_sec < 0 or spent_sec >= time_limit_sec:
                continue

            # Проверяем, есть ли хотя бы одна тема (B. x /1,00) == 0,00
            # По условию "B. 1 /1,00" ... "B. 10 /1,00"
            # У кого-то может называться чуть иначе, уточните в реальном файле
            fully_unfinished = False
            for i in range(1, 11):
                col_name = f"В. {i} /10,00"  # например "B. 1 /1,00"
                if col_name in row:
                    score_val = parse_score_1(row[col_name])
                    if score_val == 0.0:  # то есть действительно 0,00
                        fully_unfinished = True
                        break
            
            if not fully_unfinished:
                # Нет ни одной темы с 0,00
                continue

            # Если дошли сюда, значит все условия совпадают:
            #   - "Состояние" = "Завершено"
            #   - spent_sec < time_limit_sec
            #   - хотя бы одна тема == 0,00
            filtered_rows.append(row)

        # Подсчитываем результат
        count = len(filtered_rows)
        print(f"Количество людей, уложившихся в {time_limit_sec//60} мин. и имеющих хотя бы одну тему с 0,00: {count}")
        
        # Выводим список
        for r in filtered_rows:
            fio = f"{r.get('Фамилия','?')} {r.get('Имя','?')}"
            spent_str = r.get("Затраченное время", "")
            print(f"- {fio}, затраченное время: {spent_str}")

if __name__ == "__main__":
    main()
