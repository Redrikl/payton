def count_even_length_words(s: str) -> int:
    """
    Принимает строку s, в которой слова разделены пробелами.
    Возвращает количество слов, имеющих чётную длину.
    """
    words = s.split()  # Разделяем строку по пробелам
    count = 0
    for word in words:
        if len(word) % 2 == 0:
            count += 1
    return count

def main():
    user_input = input("Введите строку: ")
    result = count_even_length_words(user_input)
    print("Количество слов с чётным количеством символов:", result)

if __name__ == "__main__":
    main()
