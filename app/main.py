from flask import Flask, render_template, request
from analysis import run_descriptive, run_correlation
from model import train_model, predict_cancer

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    desc_stats = run_descriptive()  # returns a dict or HTML snippet
    return render_template("index.html", desc_stats=desc_stats)

# Correlation heatmap
@app.route("/correlation")
def correlation():
    corr_path = run_correlation()  # saves heatmap as image, returns path
    return render_template("correlation.html", corr_path=corr_path)

# Prediction page
@app.route("/predict", methods=["GET", "POST"])
def predict():
    result = None
    if request.method == "POST":
        gender = request.form["gender"]
        age = int(request.form["age"])
        smoking = int(request.form["smoking"])
        coughing = int(request.form["coughing"])
        result = predict_cancer(gender, age, smoking, coughing)
    return render_template("predict.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
