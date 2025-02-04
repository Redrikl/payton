import sqlite3
import json

def export_to_json(db_name="software.db", json_file="export.json"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    data = {}

    # Получаем все данные из таблицы tasks
    cursor.execute("""
        SELECT tasks.id, projects.name, tasks.description, tasks.status
        FROM tasks
        JOIN projects ON tasks.project_id = projects.id
    """)
    tasks = cursor.fetchall()
    
    data["tasks"] = []
    for task in tasks:
        data["tasks"].append({
            "task_id": task[0],
            "project_name": task[1],
            "description": task[2],
            "status": task[3]
        })

    # Сохраняем данные в JSON
    with open(json_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    conn.close()
    print(f"Данные экспортированы в файл {json_file}")

# Запуск экспорта
if __name__ == "__main__":
    export_to_json()
