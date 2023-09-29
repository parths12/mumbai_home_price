from flask import Flask, request, jsonify
import util

app = Flask(__name__)
util.load_saved_artifacts()

@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    area = float(request.form['area'])
    region = request.form['region']
    bhk = int(request.form['bhk'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(region,bhk,area)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Flask server for home price prediction...")
    app.run()
