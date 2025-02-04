# init_db.py
import sqlite3

def init_db():
    con = sqlite3.connect("software.db")
    cur = con.cursor()
    
    # Удаляем таблицы, если нужно «начисто»
    cur.execute("DROP TABLE IF EXISTS Tasks")
    cur.execute("DROP TABLE IF EXISTS Projects")
    cur.execute("DROP TABLE IF EXISTS Developers")
    
    # 1) Таблица разработчиков
    cur.execute("""
        CREATE TABLE Developers (
            dev_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT NOT NULL,
            skill    TEXT
        )
    """)
    
    # 2) Таблица проектов
    # Ссылается на главного разработчика (lead_dev)
    cur.execute("""
        CREATE TABLE Projects (
            proj_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT NOT NULL,
            lead_dev  INTEGER,
            FOREIGN KEY (lead_dev) REFERENCES Developers(dev_id)
        )
    """)
    
    # 3) Таблица задач
    # Каждая задача привязана к проекту и к разработчику, который её выполняет
    cur.execute("""
        CREATE TABLE Tasks (
            task_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            proj_id  INTEGER NOT NULL,
            dev_id   INTEGER NOT NULL,
            description TEXT,
            status   TEXT DEFAULT 'open',
            FOREIGN KEY (proj_id) REFERENCES Projects(proj_id),
            FOREIGN KEY (dev_id)  REFERENCES Developers(dev_id)
        )
    """)
    
    # --- Наполним тестовыми данными ---
    # Разработчики
    cur.execute("INSERT INTO Developers(name, skill) VALUES (?,?)", ("Alice", "Python"))
    cur.execute("INSERT INTO Developers(name, skill) VALUES (?,?)", ("Bob",   "C++"))
    cur.execute("INSERT INTO Developers(name, skill) VALUES (?,?)", ("Carol", "Java"))

    # Проекты (укажем lead_dev = 1 (Alice) и lead_dev=2 (Bob))
    cur.execute("INSERT INTO Projects(name, lead_dev) VALUES (?,?)", ("AlphaProject", 1))
    cur.execute("INSERT INTO Projects(name, lead_dev) VALUES (?,?)", ("BetaProject",  2))

    # Задачи
    # Привяжем к первому проекту (proj_id=1) и второму проекту (proj_id=2)
    cur.execute("INSERT INTO Tasks(proj_id, dev_id, description, status) VALUES (?,?,?,?)",
                (1, 1, "Set up repo", "done"))
    cur.execute("INSERT INTO Tasks(proj_id, dev_id, description, status) VALUES (?,?,?,?)",
                (1, 2, "Implement feature X", "open"))
    cur.execute("INSERT INTO Tasks(proj_id, dev_id, description, status) VALUES (?,?,?,?)",
                (2, 2, "Design module Y", "in-progress"))
    cur.execute("INSERT INTO Tasks(proj_id, dev_id, description, status) VALUES (?,?,?,?)",
                (2, 3, "Testing tasks", "open"))
    
    con.commit()
    con.close()

if __name__ == "__main__":
    init_db()
    print("База данных software.db успешно создана и заполнена!")
