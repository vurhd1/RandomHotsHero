from flask import Flask, render_template
import getRandomHero

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', hero="")

@app.route('/random')
def random():
    hero = getRandomHero.getRandomHero()
    print(hero)
    return render_template('home.html', hero=hero)

app.run()