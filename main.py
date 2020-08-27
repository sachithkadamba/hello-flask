# v1.1

from flask import Flask, jsonify, request
from flask_cors import CORS
from Predict_function import predict_function

app = Flask(__name__)
CORS(app)


@app.route('/health_check')
def health_check():
    return jsonify({"status":"healthy"})


@app.route('/predict_service', methods=['POST'])
def predict_service():

    return {"predictedScore": "80","predictedValue": "Contract Desktop Support"}
    
    


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8019)