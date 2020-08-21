from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/predict')
def hello_world():
    aiValue = {"predictedValue": "b9c7c11a1374e20063eadf82e144b00a", "predictionScore" : 80}
    return jsonify(aiValue)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9000)