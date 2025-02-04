import sqlite3

def run_stat_queries(db_name="software.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    print("=== Статистические запросы ===")

    # 1. Количество проектов у каждого пользователя
    print("\n1) Количество проектов у каждого пользователя:")
    cursor.execute("""
        SELECT u.name, COUNT(p.id) AS project_count
        FROM users u
        LEFT JOIN projects p ON u.id = p.user_id
        GROUP BY u.id
    """)
    for row in cursor.fetchall():
        print(f"Пользователь: {row[0]}, проектов: {row[1]}")

    # 2. Количество задач (completed) по каждому проекту
    print("\n2) Количество завершённых задач (status='completed') в каждом проекте:")
    cursor.execute("""
        SELECT p.name, COUNT(t.id) AS completed_tasks
        FROM projects p
        JOIN tasks t ON p.id = t.project_id
        WHERE t.status = 'completed'
        GROUP BY p.id
    """)
    for row in cursor.fetchall():
        print(f"Проект: {row[0]}, завершённых задач: {row[1]}")

    # 3. Пользователи с задачами в статусе 'pending'
    print("\n3) Пользователи, у которых есть задачи в статусе 'pending':")
    cursor.execute("""
        SELECT u.name, COUNT(t.id) AS pending_tasks
        FROM users u
        JOIN projects p ON u.id = p.user_id
        JOIN tasks t ON p.id = t.project_id
        WHERE t.status = 'pending'
        GROUP BY u.id
    """)
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"- {row[0]}: {row[1]} невыполненных задач")
    else:
        print("Нет пользователей с невыполненными задачами.")

    conn.close()

if __name__ == "__main__":
    run_stat_queries()
