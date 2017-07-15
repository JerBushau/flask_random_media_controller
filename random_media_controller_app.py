from flask import Flask
from flask import render_template
import random_media

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/<cat>/<num>')
def run_random_media(cat="tv", num=3):
    context = {'cat': cat, "num": num}
    if cat:
        random_media.run(cat, num)

    return render_template('result.html', **context)


app.run(debug=True, port=8000, host='0.0.0.0')
