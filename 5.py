def main():
    # Считываем N и M
    N, M = map(int, input().split())
    
    # Считываем цвета кубиков Ани
    anya_colors = set()
    for _ in range(N):
        color = int(input())
        anya_colors.add(color)
    
    # Считываем цвета кубиков Бори
    borya_colors = set()
    for _ in range(M):
        color = int(input())
        borya_colors.add(color)
    
    # Находим пересечение и разности
    common = anya_colors & borya_colors        # есть у обоих
    only_anya = anya_colors - borya_colors     # только у Ани
    only_borya = borya_colors - anya_colors    # только у Бори
    
    # Преобразуем во отсортированные списки
    common_sorted = sorted(common)
    only_anya_sorted = sorted(only_anya)
    only_borya_sorted = sorted(only_borya)
    
    # Выводим результаты.
    # 1) Пересечение
    print(len(common_sorted))
    if len(common_sorted) > 0:
        print(" ".join(map(str, common_sorted)))
    # 2) Только у Ани
    print(len(only_anya_sorted))
    if len(only_anya_sorted) > 0:
        print(" ".join(map(str, only_anya_sorted)))
    # 3) Только у Бори
    print(len(only_borya_sorted))
    if len(only_borya_sorted) > 0:
        print(" ".join(map(str, only_borya_sorted)))

if __name__ == "__main__":
    main()
# 4 3
# 0
# 1
# 2
# 10
# 9
# 1
# 2
