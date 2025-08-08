from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open('data/celebrities.json', 'r', encoding='utf-8') as f:
    celebrities = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = None
    if request.method == 'POST':
        guess = request.form['guess']
        for celeb in celebrities:
            if celeb['name'] == guess:
                feedback = celeb
                break
    return render_template('index.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)