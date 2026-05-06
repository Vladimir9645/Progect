from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
         # Определяем путь к файлу на основе URL
        if self.path == '/':
            html_file_path = 'templates/index.html'
        elif self.path == '/catalog.html':
            html_file_path = 'templates/catalog.html'
        elif self.path == '/categories':
            html_file_path = 'templates/categories.html'
        elif self.path == '/contacts':
            html_file_path = 'templates/contacts.html'
        elif self.path == '/main':
            html_file_path = 'templates/main.html'
        elif self.path == '/menu':
            html_file_path = 'menu.html'
        else:
            html_file_path = '404.html'  # страница ошибки
        
        try:
            # Открываем файл в режиме чтения текста (encoding='utf-8')
            with open(html_file_path, 'r', encoding='utf-8') as file:
                content = file.read()  # Читаем содержимое файла в строку
            
            # Отправляем ответ клиенту
            self.send_response(200)  # OK
            self.send_header('Content-type', 'text/html')  # Указываем тип контента
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))  # Отправляем HTML-код (преобразуем в байты)
            
        except FileNotFoundError:
            # Если файл не найден — отправляем ошибку 404
            self.send_error(404, 'File not found')

# Настройки сервера
host_name = 'localhost'
server_port = 8000

# Создаём и запускаем сервер
web_server = HTTPServer((host_name, server_port), MyHandler)
print(f'Сервер запущен: http://{host_name}:{server_port}')
web_server.serve_forever()

