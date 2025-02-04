import http.server
import socketserver
import os

PORT = 8000

# Указываем папку с CGI-скриптами
cgi_directory = "/cgi-bin"

# Создаём кастомный обработчик
class CustomCGIHandler(http.server.CGIHTTPRequestHandler):
    cgi_directories = [cgi_directory]

# Запускаем сервер
with socketserver.TCPServer(("", PORT), CustomCGIHandler) as httpd:
    print(f"CGI-сервер запущен на порту {PORT}")
    httpd.serve_forever()
