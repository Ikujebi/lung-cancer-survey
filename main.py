from flask import Flask, render_template, request
from analysis.descriptive_analysis import DescriptiveAnalyzer
from analysis.correlation_analysis import CorrelationAnalyzer
from analysis.machine_learning import MLAnalyzer

app = Flask(__name__)



# Home page: Descriptive statistics
@app.route("/")
def home():
    desc_analyzer = DescriptiveAnalyzer()
    desc_stats = desc_analyzer.run_descriptive()
    return render_template("index.html", desc_stats=desc_stats)

# Correlation heatmap page
@app.route("/correlation")
def correlation():
    corr_analyzer = CorrelationAnalyzer()
    corr_path = corr_analyzer.run_correlation()
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

        # Initialize MLAnalyzer here
        ml_analyzer = MLAnalyzer()
       # Call predict with keyword arguments matching your CSV/encoded features
        result = ml_analyzer.predict(
            GENDER=gender,
            AGE=age,
            SMOKING=smoking,
            COUGHING=coughing
        )
        
    return render_template("predict.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)