from flask import Flask, request
from flask_cors import CORS

from predictor.prediction import makePrediction

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    label = makePrediction(data)
    print(label)
    return label


if __name__ == '__main__':
    app.run(debug=True)
