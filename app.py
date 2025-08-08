from flask import Flask, render_template, request
import json

app = Flask(__name__)

# JSON 데이터 불러오기
with open('data/celebrities.json', encoding='utf-8') as f:
    celebrities = json.load(f)

# 정답 고정 (임시)
answer = celebrities[0]  # 예: 첫 번째 인물이 정답

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None

    if request.method == "POST":
        guess_name = request.form["guess"].strip()

        # 사용자의 추측이 리스트 안에 있는지 확인
        guess = next((person for person in celebrities if person["name"] == guess_name), None)

        if guess:
            feedback = {
                "name_match": "정답!" if guess["name"] == answer["name"] else "틀림",
                "age_match": "같음" if guess["age"] == answer["age"] else f"다름 ({guess['age']}세)",
                "field_match": "같음" if guess["field"] == answer["field"] else f"다름 ({guess['field']})",
                "agency_match": "같음" if guess["agency"] == answer["agency"] else f"다름 ({guess['agency']})",
            }
        else:
            feedback = {"name_match": "존재하지 않는 인물입니다", "age_match": "", "field_match": "", "agency_match": ""}

    return render_template("index.html", feedback=feedback)