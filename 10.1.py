# stats_queries.py
import sqlite3

def run_stats():
    con = sqlite3.connect("software.db")
    cur = con.cursor()
    
    # 1) Сколько задач у каждого разработчика
    print("=== Количество задач по разработчикам ===")
    cur.execute("""
        SELECT d.name, COUNT(t.task_id)
        FROM Developers d
        LEFT JOIN Tasks t ON d.dev_id = t.dev_id
        GROUP BY d.dev_id
    """)
    for row in cur.fetchall():
        print(f"Разработчик {row[0]}: {row[1]} задач")

    # 2) Список проектов, у которых >= 2 задач
    print("\n=== Проекты с двумя и более задачами ===")
    cur.execute("""
        SELECT p.name, COUNT(t.task_id) AS cnt
        FROM Projects p
        JOIN Tasks t ON p.proj_id = t.proj_id
        GROUP BY p.proj_id
        HAVING cnt >= 2
    """)
    for row in cur.fetchall():
        print(f"Проект {row[0]} -> {row[1]} задач")

    # 3) Сколько задач уже закрыты (status='done')
    print("\n=== Сколько задач завершены ===")
    cur.execute("""
        SELECT COUNT(*)
        FROM Tasks
        WHERE status='done'
    """)
    done_count = cur.fetchone()[0]
    print(f"Завершённых задач: {done_count}")

    con.close()

if __name__ == "__main__":
    run_stats()
