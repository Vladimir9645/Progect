from flask import Flask, request, send_file

app = Flask(__name__)

# Маршрут для GET-запросов — возвращает страницу «Контакты»
@app.route('/', methods=['GET'])
def get_contacts():
    # Читаем содержимое HTML-файла
    with open('contacts.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Устанавливаем тип контента text/html (вместо application/json)
    return html_content, 200, {'Content-Type': 'text/html'}

# Маршрут для POST-запросов (дополнительное задание)
@app.route('/', methods=['POST'])
def handle_post():
    # Получаем данные, отправленные пользователем
    data = request.form  # Для данных из формы
    json_data = request.get_json()  # Для JSON-данных

    # Печатаем данные в консоль
    print("Данные из формы:", dict(data))
    print("JSON-данные:", json_data)

    return 'Данные получены!', 200

if __name__ == '__main__':
    app.run(debug=True)
