from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brenden'}
    recipes = [
        {
            'author': {'username': 'Lotta'},
            'title': 'Cooking... Yay'
        },
        {
            'author': {'username': 'Brenden'},
            'title': 'Peanut Butter... It just peanuts'
        }
    ]
    return render_template('index.html', title='Home', user=user, recipes=recipes)