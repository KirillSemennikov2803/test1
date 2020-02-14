from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("start.html")


@app.route('/q1')
def q1():
    return render_template("quiz.html", title="Первый вопрос!", q0="1 + 1 - 1 =?", q1="2", q2="1", q3="Пути "
                                                                                                      "господни "
                                                                                                      "неисповедимы",
                           q4="15", url="/q2")


@app.route('/q2')
def q2():
    return render_template("quiz.html", title="ПОздравляю Вы Правильно ответили на Вопрос", q0="Сколько Весит Слон?",
                           q1="1 тонну", q2="5 Тонн", q3="Пути "
                                                         "господни "
                                                         "неисповедимы",
                           q4="15 кг", url="/q3")


@app.route('/q3')
def q3():
    return render_template("quiz.html", title="Ничего Себе Вы почти у цели", q0="Сколько в Казани Колес обозрения",
                           q1="1", q2="2", q3="Пути "
                                              "господни "
                                              "неисповедимы",
                           q4="-3", url="/q4")


@app.route('/q4')
def q4():
    return render_template("quiz.html", title="Финальный вопрос,Он самый сложный но я верю ты справишься",
                           q0="Какой Элемент у пикачу",
                           q1="Молния", q2="Молния", q3="Молния",
                           q4="-Молния", url="/final")


@app.route('/final')
def final():
    return render_template("final.html")


@app.route('/final2')
def final2():
    return send_file("котя.PNG")


if __name__ == '__main__':
    app.run()
