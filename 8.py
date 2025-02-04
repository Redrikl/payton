import re

def is_phone_number(s: str) -> bool:
    """
    Проверяет, является ли строка s телефонным номером по следующему критерию:
    - Опционально начинается с '+'
    - Затем содержит только цифры
    - Суммарное количество цифр от 10 до 15
    """
    pattern = r"^\+?\d{10,15}$"
    return bool(re.match(pattern, s))

def validate_phone_number(s: str) -> str:
    """
    Возвращает строку s, если она является корректным телефонным номером.
    Если проверка не пройдена, выбрасывает ValueError (реальное исключение).
    """
    if not is_phone_number(s):
        raise ValueError("Некорректный телефонный номер!")
    return s

def main():
    user_input = input("Введите предполагаемый телефонный номер: ")
    try:
        valid_phone = validate_phone_number(user_input)
        print("Телефонный номер корректен:", valid_phone)
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()

#+71234567890