from math import gcd

def is_prime(x: int) -> bool:
    """
    Проверяет, является ли число x простым.
    """
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def max_prime_divisor(n: int) -> int:
    """
    1) Найти максимальный простой делитель числа n.
    """
    # Будем факторизовать |n|
    num = abs(n)
    answer = 1  # На случай, если у числа нет простых делителей (напр. n=±1,0)

    # Убираем из num все деления на 2
    while num % 2 == 0 and num > 1:
        answer = 2
        num //= 2

    # Далее проверяем нечётные делители
    d = 3
    while d * d <= num:
        while num % d == 0:
            answer = d
            num //= d
        d += 2

    # Если после всех делений num > 1, значит это простое число
    if num > 1:
        answer = num

    return answer

def second_function(n: int) -> int:
    """
    2) Найти произведение цифр числа, которые не делятся на 5.
       (То есть исключаем цифры 0 и 5.)
    """
    num = abs(n)
    product = 1
    has_digit = False  # Чтобы отследить, были ли вообще цифры, не делящиеся на 5

    if num == 0:
        # У числа '0' единственная цифра '0', она делится на 5
        # Тогда произведение таких цифр — формально 1 (пустое произведение).
        return 1

    while num > 0:
        digit = num % 10
        if digit % 5 != 0:  # digit не 0 и не 5
            product *= digit
            has_digit = True
        num //= 10

    return product if has_digit else 1

def max_odd_composite_divisor(n: int) -> int:
    """
    Вспомогательная функция: ищем максимальный нечётный
    непростой (составной) делитель числа n.
    Если такого нет, вернёт 1 или 0 — на ваше усмотрение.
    """
    num = abs(n)
    max_div = 1  # если не найдём ни одного подходящего, оставим 1

    # Перебираем делители: для каждого i, если i делит num,
    # то num//i тоже делитель
    # Ищем по сути в паре (i, num//i).
    i = 1
    while i * i <= num:
        if num % i == 0:
            # Проверяем i
            if i > 1 and i % 2 == 1 and (not is_prime(i)):
                # нечётный, больше 1, и составной
                max_div = max(max_div, i)

            # Проверяем пару num//i
            other = num // i
            if other > 1 and other % 2 == 1 and (not is_prime(other)):
                max_div = max(max_div, other)
        i += 1

    return max_div

def third_function(n: int) -> int:
    """
    3) Найти НОД между:
       - максимальным нечётным непростым делителем числа
       - и произведением всех цифр этого числа
    """
    # Сначала найдём максимальный нечётный непростой делитель
    max_div = max_odd_composite_divisor(n)

    # Теперь найдём произведение всех цифр числа n
    # (именно всех цифр, независимо от делимости на 5)
    num = abs(n)
    product_all = 1
    if num == 0:
        # Единственная цифра: 0
        product_all = 0
    else:
        while num > 0:
            digit = num % 10
            product_all *= digit
            num //= 10

    # Ищем НОД
    return gcd(max_div, product_all)

# ----------------------
# Пример использования:
if __name__ == "__main__":
    test_number = 360  # Возьмём для наглядности

    # 1) Максимальный простой делитель
    print("Максимальный простой делитель числа:", max_prime_divisor(test_number))

    # 2) Произведение цифр, не делящихся на 5
    print("Произведение цифр, не делящихся на 5:", second_function(test_number))

    # 3) НОД(макс. нечётного непростого делителя, произведения всех цифр)
    print("НОД нужных величин:", third_function(test_number))

