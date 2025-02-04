#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sqlite3

cgitb.enable()  # Показывать трассировку ошибок в браузере

# ВАЖНО: указываем корректный заголовок с UTF-8
print("Content-Type: text/html; charset=windows-1251\n")

# Считываем данные из формы
form = cgi.FieldStorage()
project_id = form.getfirst("project_id", "")  # какой проект
description = form.getfirst("description", "") # описание задачи
status = form.getfirst("status", "")           # статус ('pending', 'completed', etc.)

# Подключаемся к базе (возможно, нужно скорректировать путь):
# Если software.db лежит на уровень выше папки cgi-bin:
conn = sqlite3.connect("software.db")
cursor = conn.cursor()

msg = ""

# Если все поля заполнены, добавляем запись в таблицу tasks
if project_id and description and status:
    try:
        cursor.execute("""
            INSERT INTO tasks (project_id, description, status)
            VALUES (?, ?, ?)
        """, (project_id, description, status))
        conn.commit()
        msg = "Задача успешно добавлена!"
    except Exception as e:
        msg = f"Ошибка при добавлении задачи: {e}"

# Выводим HTML
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
except Exception as e:
    print(f"<p style='color:red;'>Ошибка при выборке задач: {e}</p>")

print("</body></html>")

conn.close()