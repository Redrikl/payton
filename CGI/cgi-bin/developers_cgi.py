#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sqlite3

# Включаем режим отладки (показывает трассировку ошибок в браузере)
cgitb.enable()

# Печатаем заголовок HTTP‑ответа, сообщая, что будет выдан HTML
print("Content-Type: text/html; charset=utf-8\n")

# Получаем данные формы (если это POST-запрос)
form = cgi.FieldStorage()

# Начинаем вывод HTML
print("<html><head><title>Developers Table</title></head><body>")
print("<h1>Добавление нового разработчика в таблицу 'Developers'</h1>")

# Если пришли поля формы (name, skill), пробуем добавить запись в БД
if form and "name" in form and "skill" in form:
    dev_name  = form.getvalue("name")
    dev_skill = form.getvalue("skill")

    con = sqlite3.connect("software.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Developers(name, skill) VALUES (?,?)",
                    (dev_name, dev_skill))
        con.commit()
        print("<p style='color:green;'>Новый разработчик успешно добавлен!</p>")
    except Exception as e:
        print(f"<p style='color:red;'>Ошибка при добавлении: {e}</p>")
    finally:
        con.close()

# Форма для ввода данных нового разработчика
print("""
<form method="POST" action="developers_cgi.py">
  <label>Имя разработчика:</label><br>
  <input type="text" name="name" value="Alice"><br><br>

  <label>Навык (skill):</label><br>
  <input type="text" name="skill" value="Python"><br><br>

  <input type="submit" value="Добавить">
</form>
<hr>
""")

# Теперь выводим актуальное содержимое таблицы Developers
print("<h2>Текущие разработчики (Developers):</h2>")
print("<table border='1'><tr><th>ID</th><th>Name</th><th>Skill</th></tr>")

con = sqlite3.connect("software.db")
cur = con.cursor()
cur.execute("SELECT dev_id, name, skill FROM Developers ORDER BY dev_id")
for row in cur.fetchall():
    print("<tr>")
    print(f"<td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td>")
    print("</tr>")
con.close()

print("</table></body></html>")
