#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sqlite3

# Включаем вывод traceback при ошибках (для отладки)
cgitb.enable()

# Заголовок, необходимый для вывода HTML через CGI
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

print("<html><head><title>Software DB</title></head><body>")
print("<h1>Добавление задачи в базу 'software.db'</h1>")

# Проверяем, не пришёл ли POST‑запрос с нужными полями
if form and "proj_id" in form and "dev_id" in form and "description" in form:
    proj_id_str = form.getvalue("proj_id")
    dev_id_str  = form.getvalue("dev_id")
    desc_str    = form.getvalue("description")
    status_str  = form.getvalue("status", "open")  # по умолчанию "open"

    # Открываем базу и вставляем новую задачу
    con = sqlite3.connect("software.db")
    cur = con.cursor()
    try:
        cur.execute("""
            INSERT INTO Tasks(proj_id, dev_id, description, status)
            VALUES (?,?,?,?)
        """, (proj_id_str, dev_id_str, desc_str, status_str))
        con.commit()
        print("<p style='color:green;'>Новая задача успешно добавлена!</p>")
    except Exception as e:
        print(f"<p style='color:red;'>Ошибка при добавлении: {e}</p>")
    finally:
        con.close()

# Выводим форму
print("""
<form method="POST" action="software_cgi.py">
  <label>Project ID: <input type="text" name="proj_id" value="1"></label><br><br>
  <label>Developer ID: <input type="text" name="dev_id" value="1"></label><br><br>
  <label>Description: <input type="text" name="description" value="New task"></label><br><br>
  <label>Status:
    <select name="status">
      <option value="open">open</option>
      <option value="in-progress">in-progress</option>
      <option value="done">done</option>
    </select>
  </label><br><br>
  <input type="submit" value="Добавить задачу">
</form>
<hr>
""")

# Выводим всю таблицу Tasks
print("<h2>Список задач (Tasks):</h2>")
print("<table border='1'><tr><th>ID</th><th>ProjID</th><th>DevID</th><th>Description</th><th>Status</th></tr>")

con = sqlite3.connect("software.db")
cur = con.cursor()
cur.execute("SELECT task_id, proj_id, dev_id, description, status FROM Tasks")
for row in cur.fetchall():
    print("<tr>")
    print(f"<td>{row[0]}</td>")
    print(f"<td>{row[1]}</td>")
    print(f"<td>{row[2]}</td>")
    print(f"<td>{row[3]}</td>")
    print(f"<td>{row[4]}</td>")
    print("</tr>")
con.close()

print("</table></body></html>")
