def read_input(filename):
    """
    Читает входные данные из файла.
    Возвращает N, K и список измерений M.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    
    # Считываем N и K
    N, K = map(int, lines[0].split())
    
    # Считываем N измерений (индексация в Python идёт с 0, поэтому ничего не добавляем)
    M = list(map(int, lines[1:N+1]))

    return N, K, M

def max_sum_with_step(N, K, M):
    """
    Вычисляет максимальную сумму трёх измерений, 
    выбирая индексы с интервалом не менее K.
    """
    # Используем отрицательную бесконечность для начального состояния
    NEG_INF = float('-inf')
    
    # Инициализируем массивы для динамического хранения результатов
    best1 = [NEG_INF] * N  # Максимальное 1-е число до момента i
    best2 = [NEG_INF] * N  # Максимальная сумма 2-х чисел до i
    best3 = [NEG_INF] * N  # Максимальная сумма 3-х чисел до i
    
    # Проходим по каждому измерению
    for i in range(N):
        # best1[i]: наибольшее значение M[j] среди первых i-K измерений
        best1[i] = best1[i-1] if i > 0 else NEG_INF
        if i - K >= 0:
            best1[i] = max(best1[i], M[i - K])
        
        # best2[i]: максимум суммы двух измерений, соблюдая шаг K
        best2[i] = best2[i-1] if i > 0 else NEG_INF
        if i - K >= 0 and best1[i] != NEG_INF:
            best2[i] = max(best2[i], M[i] + best1[i])  # M[i] — текущее измерение
        
        # best3[i]: максимум суммы трёх измерений, соблюдая шаг K
        best3[i] = best3[i-1] if i > 0 else NEG_INF
        if i - K >= 0 and best2[i - K] != NEG_INF:
            best3[i] = max(best3[i], M[i] + best2[i - K])
    
    # Итоговая максимальная сумма трёх измерений
    return best3[N-1]  # Последний элемент хранит искомое значение

def main():
    # Читаем входные данные из файлов A и B
    N_A, K_A, M_A = read_input("27-168a.txt")
    N_B, K_B, M_B = read_input("27-168.txt")
    
    # Решаем задачу для обоих файлов
    result_A = max_sum_with_step(N_A, K_A, M_A)
    result_B = max_sum_with_step(N_B, K_B, M_B)
    
    # Выводим результат для файла A
    print("Максимальная сумма (Файл A):", result_A)
    # Выводим результат для файла B
    print("Максимальная сумма (Файл B):", result_B)

if __name__ == "__main__":
    main()
