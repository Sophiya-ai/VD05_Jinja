from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context={
        'question' : 'Тайна происхождения эльфов',
        'active_page' : 'home'
    }
    return render_template("home.html", **context) #распаковываем словарь и пробрасываем наши переменные

@app.route("/about/")
def about():
    context = {
        'question': 'Тайны быта эльфов',
        'active_page': 'about'
    }
    return render_template("about.html", **context)

app.run()