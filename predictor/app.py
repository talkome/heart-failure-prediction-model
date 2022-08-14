from flask import Flask, request
from predictor.prediction import func

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    label = func(data)
    return label


if __name__ == '__main__':
    app.run(debug=True)
