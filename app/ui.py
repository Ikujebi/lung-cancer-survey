from flask import Flask, render_template, request
from analysis.correlation_analysis import run_correlation
from analysis.descriptive_analysis import run_descriptive
from analysis.machine_learning import run_model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descriptive')
def descriptive():
    run_descriptive()
    return "Descriptive analysis complete! Check the plots."

@app.route('/correlation')
def correlation():
    run_correlation()
    return "Correlation analysis complete! Check the heatmap."

@app.route('/ml')
def ml():
    run_model()
    return "Machine learning model trained and evaluated! Check the console and plots."

if __name__ == '__main__':
    app.run(debug=True)
