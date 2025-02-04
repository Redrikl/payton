def main():
    n = int(input().strip())
    
    # Создаём словарь (в Python – dict), в котором 
    # оба слова пары будут указывать друг на друга.
    synonyms = {}
    
    # Считываем пары «синоним – синоним»
    for _ in range(n):
        word1, word2 = input().split()
        synonyms[word1] = word2
        synonyms[word2] = word1
    
    # Считываем слово, для которого нужно найти синоним
    query = input().strip()
    
    # Выводим синоним из словаря
    if query in synonyms:
        print(synonyms[query])
    else:
        print("Синоним не найден")  # На случай, если вдруг нет такого слова

if __name__ == "__main__":
    main()
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
