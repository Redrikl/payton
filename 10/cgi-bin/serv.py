#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sqlite3

cgitb.enable()  # для отладки

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

# Форма может содержать поля для добавления нового ПО:
# Поля: title, developer_id, category_id, release_year
title = form.getfirst("title", "")
developer_id = form.getfirst("developer_id", "")
category_id = form.getfirst("category_id", "")
release_year = form.getfirst("release_year", "")

conn = sqlite3.connect("D:/User/Documents/GitHub/payton/10/software.db")  # путь к вашей БД
cursor = conn.cursor()

# Если форма отправлена и поля заполнены, то вставляем новую запись
if title and developer_id and category_id and release_year:
    try:
        cursor.execute("""
            INSERT INTO software(title, developer_id, category_id, release_year)
            VALUES (?, ?, ?, ?)
        """, (title, developer_id, category_id, release_year))
        conn.commit()
        msg = f"Успешно добавлено ПО: {title}"
    except Exception as e:
        msg = f"Ошибка при добавлении: {e}"
else:
    msg = ""

# Выводим HTML‑страницу
print(f"""
<html>
<head>
    <meta charset="utf-8">
    <title>CGI‑пример</title>
</head>
<body>
    <h1>Добавить новое ПО</h1>
    <form method="POST" action="cgi_server.py">
        <label>Название: <input type="text" name="title" value="{title}"></label><br>
        <label>ID Разработчика: <input type="text" name="developer_id" value="{developer_id}"></label><br>
        <label>ID Категории: <input type="text" name="category_id" value="{category_id}"></label><br>
        <label>Год релиза: <input type="text" name="release_year" value="{release_year}"></label><br>
        <input type="submit" value="Добавить">
    </form>
    <p style="color:green;">{msg}</p>
    <hr>
    <h2>Содержимое таблицы software</h2>
""")

# Выведем содержимое таблицы software
cursor.execute("""
    SELECT software_id, title, developer_id, category_id, release_year
    FROM software
""")
rows = cursor.fetchall()

print("<table border='1'>")
print("<tr><th>ID</th><th>Название</th><th>DevID</th><th>CatID</th><th>Год</th></tr>")
for r in rows:
    print(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>")
print("</table>")

print("""
</body>
</html>
""")

conn.close()
