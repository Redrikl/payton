#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

def init_db(db_name="software.db"):
    """Создаёт таблицы users, projects, tasks в базе данных."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    """)

    # Таблица проектов
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    # Таблица задач
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        FOREIGN KEY (project_id) REFERENCES projects(id)
    );
    """)

    conn.commit()
    conn.close()
    print("Таблицы созданы или уже существуют.")

def insert_sample_data(db_name="software.db"):
    """Добавляет тестовые записи в таблицы users, projects, tasks."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Очистим таблицы для добавления новых данных
    cursor.execute("DELETE FROM tasks;")
    cursor.execute("DELETE FROM projects;")
    cursor.execute("DELETE FROM users;")

    # Добавляем пользователей
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Никита", "nikita@example.com"))
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Анна", "anna@example.com"))

    # Добавляем проекты
    cursor.execute("INSERT INTO projects (name, user_id) VALUES (?, ?)", ("Проект X", 1))
    cursor.execute("INSERT INTO projects (name, user_id) VALUES (?, ?)", ("Проект Y", 2))

    # Добавляем задачи
    cursor.execute("INSERT INTO tasks (project_id, description, status) VALUES (?, ?, ?)",
                   (1, "Разработка интерфейса", "pending"))
    cursor.execute("INSERT INTO tasks (project_id, description, status) VALUES (?, ?, ?)",
                   (2, "Тестирование модуля", "in progress"))
    cursor.execute("INSERT INTO tasks (project_id, description, status) VALUES (?, ?, ?)",
                   (2, "Документация", "completed"))

    conn.commit()
    conn.close()
    print("Тестовые данные добавлены.")

if __name__ == "__main__":
    init_db()
    insert_sample_data()
    print("Инициализация БД завершена!")
