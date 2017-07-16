from flask import Flask
from flask import render_template
import random_media

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

manager = random_media.Manager()

@app.route('/api/<cat>/<num>')
def run_random_media(cat="tv", num=3):
    context = {'cat': cat, "num": num}
    if cat and manager.player.is_playing() == 0:
        manager.play(cat, num)
        return '', 200
    else:
        return '', 500

@app.route('/api/next')
def next():
    manager.next()
    return '', 200


@app.route('/api/prev')
def prev():
    manager.prev()
    return '', 200


@app.route('/api/stop')
def destroy():
    manager.stop()
    return '', 200

app.run(debug=True, port=8000, host='0.0.0.0')
