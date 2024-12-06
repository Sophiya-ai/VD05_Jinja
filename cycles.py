from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def net():
    context={
        'caption' : "Сетка",
        'user' : "Нина",
        'number' : 8,
        'list' : ["Nina","Karina","Anton","Nikita"],
        'poem' : ["Сижу за решёткой в темнице сырой.",
                "Вскормленный в неволе орёл молодой,",
                "Мой грустный товарищ, махая крылом,",
                "Кровавую пищу клюёт под окном,",
                "Клюёт, и бросает, и смотрит в окно,",
                "Как будто со мною задумал одно."]
    }
    return render_template("shablon.html", **context) #распаковываем словарь и пробрасываем наши переменные

@app.route("/shablon/")
def net2():
    context = {
        'caption': "Сетка шаблон",
        'link': "Перейти дальше"
    }
    return render_template("cw_setka.html", **context)

@app.route("/card/")
def card():
    return render_template("card.html")



#if __name__ == "__main__":
app.run()