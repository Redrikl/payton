import random

def shuffle_words_in_string(s: str) -> str:
    """
    Принимает строку s, в которой слова разделены пробелами.
    Возвращает новую строку, где порядок слов перемешан случайным образом.
    """
    words = s.split()
    random.shuffle(words)
    return " ".join(words)

def main():
    # Считываем строку из терминала
    # user_input = "здесь какие-то слова для примера"
    user_input = input("Введите строку: ")
    # Вызываем функцию перемешивания
    shuffled = shuffle_words_in_string(user_input)
    # Выводим результат
    print("Перемешанная строка:", shuffled)

if __name__ == "__main__":
    main()
