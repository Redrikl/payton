import sqlite3
import json

def import_from_json(db_name="software.db", json_file="export.json"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Открываем JSON файл и загружаем данные
    with open(json_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Очищаем таблицу tasks перед импортом новых данных
    cursor.execute("DELETE FROM tasks;")

    # Добавляем данные в таблицу tasks
    for task in data["tasks"]:
        cursor.execute("""
            INSERT INTO tasks (project_id, description, status)
            VALUES (
                (SELECT id FROM projects WHERE name = ?),
                ?, ?
            )
        """, (task["project_name"], task["description"], task["status"]))

    conn.commit()
    conn.close()
    print(f"Данные импортированы из файла {json_file}")

# Запуск импорта
if __name__ == "__main__":
    import_from_json()
