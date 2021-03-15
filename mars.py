from flask import Flask

app = Flask(__name__)

@app.route('/')
def ship():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    promotion_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.", "Мы сделаем обитаемыми безжизненные пока планеты.", 
    "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(promotion_list)

@app.route('/image_mars')
def image():
   return"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.gif" alt="Жди нас, Марс!">
                    <h1>Вот она какая, красная планета</h1>
                  </body>
                </html>"""

@app.route('/promotion_image')
def bootstrap():
    return '''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1><span style="color: #ff0000;"><strong>Жди нас, Марс!</strong></span></h1>
                    <img src="/static/img/mars.gif">
                    <div class="alert alert-primary" role="alert" style="background-color: #ff9999; color: #aa0000;">
                     Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #99ff99; color: #00aa00;">
                     Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #9999ff; color: #0000aa;">
                     Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #ffff99; color: #aaaa00;">
                     И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #ff99ff;color: #aa00aa;">
                     Присоединяйся!
                    </div>

                  </body>
                </html>'''


if __name__ == "__main__":
    app.run(port=8080, debug=True)
