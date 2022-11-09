from flask import Flask, render_template, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from main import interpret
from const import SEARCH_HISTORY, INSERT_HISTORY_OBJECT


TO_PRINT_TYPES = {
    'BinaryDigit': 'integer',
    'str': 'char'
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/pascal_interpreter'
db = SQLAlchemy(app)


@app.route('/')
def index():
    """
    Главная страница
    :return:
    """
    history = get_history()
    return render_template('index.html', history=history)


@app.route('/run/', methods=['POST'])
def run_interpreter():
    """
    Выполнить запрос
    :return:
    """
    code = request.form.get('code')
    if not code:
        return index()
    if '"' in code:
        history = get_history()
        return render_template('index.html',
                               history=history,
                               has_result=True,
                               print_data='Возникла ошибка:\nНедопустимый символ: "')

    interpreter, error, optimized_code = None, None, None
    try:
        history_code = prepare_code_to_write_history(code)
        db.session.execute(INSERT_HISTORY_OBJECT.format(history_code))
        db.session.commit()
        interpreter = interpret(code)
        if request.form.get('optimize'):
            optimized_code = interpreter.get_optimized_code()
    except Exception as exc:
        error = f'Возникла ошибка:\n{exc}'

    declare_scope = {key: TO_PRINT_TYPES.get(value.__name__) for key, value in interpreter.declare_scope.items()} if interpreter else None
    global_scope = interpreter.global_scope if interpreter else None
    print_data = interpreter.print_str if interpreter else str(error)
    history = get_history()

    return render_template('index.html',
                           code=code,
                           history=history,
                           has_result=True,
                           declare_scope=declare_scope,
                           global_scope=global_scope,
                           print_data=print_data,
                           optimized_code=optimized_code)


def get_history():
    """
    Хелпер получения истории ввода интерпретатора - 50 ближайших записей
    :return:
    """
    data = db.session.execute(SEARCH_HISTORY)
    return [item[0] for item in data]


def prepare_code_to_write_history(text: str):
    """
    Подготовить текст для записи в БД
    :param text: исходный код
    :return: код с экранированными одинарными ковычками
    """
    return text.replace("'", "''")


if __name__ == '__main__':
    app.debug = True
    app.run()
