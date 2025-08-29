
from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

categories = [
    "P/C change", "Pin alignment", "wafer alignment", "clean recipe setup",
    "ODSP", "probe mark inspection", "PMI check", "Spec read"
]

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
        emp_a = request.form['emp_a_name']
        emp_b = request.form['emp_b_name']
        return render_template("evaluate.html", emp_a=emp_a, emp_b=emp_b, categories=categories)
    return render_template("form.html")

@app.route('/evaluate', methods=['POST'])
def evaluate():
    emp_a = request.form['emp_a']
    emp_b = request.form['emp_b']
    employees = [emp_a, emp_b]
    scores = {emp: [] for emp in employees}
    for emp in employees:
        for cat in categories:
            val = int(request.form[f"{emp}_{cat}"])
            scores[emp].append(val)

    df = pd.DataFrame(scores, index=categories)
    df.to_excel("training_app/static/training_scores.xlsx", engine="openpyxl")

    labels = np.array(categories)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 5), subplot_kw=dict(polar=True))
    for emp, vals in scores.items():
        data = vals + vals[:1]
        ax.plot(angles, data, label=emp)
        ax.fill(angles, data, alpha=0.25)

    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    plt.title("Training Radar Chart")
    plt.legend(loc='upper right')
    plt.savefig("training_app/static/training_radar_chart.png")

    return "已成功提交評分並產生 Excel 與雷達圖。請查看 static 資料夾。"

if __name__ == '__main__':
    app.run(debug=True)
