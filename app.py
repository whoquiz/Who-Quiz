from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

with open('data/celebrities.json', encoding='utf-8') as f:
    data = json.load(f)

# 무작위 인물 고르기
current = random.choice(data)

@app.route("/", methods=["GET", "POST"])
def index():
    global current
    result = ""

    if request.method == "POST":
        guess = request.form.get("guess")
        if guess.strip() == current["이름"]:
            result = "🎉 정답입니다!"
            current = random.choice(data)
        else:
            result = f"❌ 오답입니다. 정답은 {current['이름']}!"

    return render_template("index.html", person=current, result=result)

if __name__ == "__main__":
    app.run()