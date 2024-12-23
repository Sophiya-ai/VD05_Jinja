from flask import Flask, render_template

#Создаём переменную и сохраняем в неё объект класса Flask. Переменная name — это специальная переменная
# в Python, она содержит в себе имя текущего модуля, помогает фреймворку находить нужные ресурсы,
# шаблоны истатические файлы
app = Flask(__name__)

#route — конкретный декоратор. Он нужен для того, чтобы позже мы могли прописать URL-адрес страницы.
# Этот декоратор используется для того, чтобы мы прописывали маршруты, присваивали функциям ссылки и URL-адреса.
# Главная страница обозначается одним слешем (/) — та страница, которая открывается после захода на сайт.
# Это не конкретный адрес, а дополнение к адресу.
# Переменные мы обозначаем треугольными скобками <>. Теперь мы можем написать любое дополнение в адресную строку,
# и это дополнение будет выводиться на сайте после “Привет”.
# @app.route("/")
# @app.route("/<password>/")
# def hello(password=None):
#     if password == '1234':
#         return f"Доступ разрешен"
#     else:
#         return f"Доступ запрещен"
#
#
# #если прописано более 1 адреса, т у нас множественное декорирование
# @app.route("/new/")
# @app.route("/newpage/")
# @app.route("/новаястраница/")
# def new():
#     return "new page"


#вариант работы с html
# @app.route("/")
# def hello():
#     html="""
#     <h1>тестовый запуск локального сервера</h1>
#     <p>а это просто текст</p>
#     """
#     return html


@app.route("/")
def net():
    context={
        'caption' : "Сетка",
        'link' : "Куда-то перейти"
    }
    #return render_template("cw_setka.html", caption="Сетка", link="Куда-то перейти")
    return render_template("cw_setka.html", **context) #распаковываем словарь и пробрасываем наши переменные

@app.route("/shablon/")
def net2():
    context = {
        'caption': "Сетка шаблон",
        'link': "Перейти дальше"
    }
    #return render_template("cw_setka.html", caption="Сетка шаблон", link="Перейти дальше")
    return render_template("cw_setka.html", **context)

@app.route("/card/")
def card():
    return render_template("card.html")



#if __name__ == "__main__":
app.run()