from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

# 정답 데이터 로드
with open('data/celebrities.json', 'r', encoding='utf-8') as f:
    celebrities = json.load(f)

# 하나 랜덤으로 고름
target = random.choice(celebrities)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        guess = request.form["guess"]
        if guess.strip() == target["name"]:
            message = f"🎉 정답입니다! {target['name']}을(를) 맞히셨어요!"
        else:
            message = "❌ 틀렸습니다. 다시 시도해보세요!"

    # 정답의 힌트 전달
    hint = {
        "profession": target["profession"],
        "agency": target["agency"],
        "age": target["age"]
    }

    return render_template("index.html", hint=hint, message=message)

if __name__ == "__main__":
    app.run(debug=True)