from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

with open("data/celebrities.json", "r", encoding="utf-8") as f:
    celebs = json.load(f)

# 오늘의 정답 (간단하게 첫 번째 인물로 설정)
ANSWER = celebs[0]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        guess = next((c for c in celebs if c["name"] == name), None)
        if guess:
            result = compare_celebs(guess, ANSWER)
        else:
            result = {"에러": "해당 인물을 찾을 수 없습니다."}
    return render_template("index.html", result=result, answer_name=ANSWER["name"])

def compare_celebs(guess, answer):
    feedback = {}
    now = datetime.now()
    feedback["이름"] = "✅" if guess["name"] == answer["name"] else "❌"
    feedback["성별"] = "✅" if guess["gender"] == answer["gender"] else "❌"
    feedback["나이"] = compare_age(guess["birth_year"], answer["birth_year"])
    feedback["분야"] = "✅" if any(f in answer["fields"] for f in guess["fields"]) else "❌"
    feedback["소속사"] = "✅" if guess["agency"] == answer["agency"] else "❌"
    return feedback

def compare_age(g_year, a_year):
    g_age = datetime.now().year - g_year
    a_age = datetime.now().year - a_year
    if g_age == a_age:
        return "✅ 동일"
    elif g_age > a_age:
        return "🔻 더 많음"
    else:
        return "🔺 더 적음"

if __name__ == "__main__":
    app.run(debug=True)
