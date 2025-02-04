#!/usr/bin/env python3
# -*- coding: cp1251 -*-

import cgi
import cgitb
import sqlite3

cgitb.enable()  # Показывать ошибки в браузере

# Указываем заголовок с кодировкой windows-1251
print("Content-Type: text/html; charset=windows-1251\n")

# Получаем данные из формы
form = cgi.FieldStorage()
project_id = form.getfirst("project_id", "").strip()  # ID проекта
description = form.getfirst("description", "").strip()  # Описание задачи
status = form.getfirst("status", "").strip()  # Статус задачи

msg = ""

# Проверка, что все поля формы были заполнены
if project_id and description and status:
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect("../software.db")
        cursor = conn.cursor()

        # Добавление новой задачи в таблицу tasks
        cursor.execute("""
            INSERT INTO tasks (project_id, description, status)
            VALUES (?, ?, ?)
        """, (project_id, description, status))

        # Фиксация изменений в базе данных
        conn.commit()

        # Закрытие соединения
        conn.close()

        msg = "Задача успешно добавлена!"
    except Exception as e:
        msg = f"Ошибка при добавлении задачи: {e}"
else:
    msg = "Пожалуйста, заполните все поля."

# Начало HTML-страницы
print(f"""
<html>
<head>
    <meta charset="windows-1251">
    <title>Добавить задачу</title>
</head>
<body>
    <h1>Добавить задачу</h1>
    <form method="POST" action="script.py">
        <label>ID проекта:
            <input type="text" name="project_id" value="{project_id}">
        </label><br><br>
        <label>Описание задачи:
            <input type="text" name="description" value="{description}">
        </label><br><br>
        <label>Статус задачи:
            <input type="text" name="status" value="{status}">
        </label><br><br>

        <input type="submit" value="Сохранить">
    </form>

    <p style="color:green;">{msg}</p>
    <hr>
    <h2>Список задач</h2>
""")

# Выводим таблицу задач с данными о проекте
try:
    # Подключаемся к базе данных
    conn = sqlite3.connect("../software.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tasks.id, projects.name, tasks.description, tasks.status
        FROM tasks
        JOIN projects ON tasks.project_id = projects.id
    """)
    rows = cursor.fetchall()

    print("<table border='1'>")
    print("<tr><th>ID задачи</th><th>Проект</th><th>Описание</th><th>Статус</th></tr>")
    for (task_id, project_name, desc, st) in rows:
        print(f"<tr><td>{task_id}</td><td>{project_name}</td><td>{desc}</td><td>{st}</td></tr>")
    print("</table>")

    # Закрытие соединения
    conn.close()
except Exception as e:
    print(f"<p style='color:red;'>Ошибка при выборке задач: {e}</p>")

print("</body></html>")
