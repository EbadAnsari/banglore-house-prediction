from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__, static_folder="static", template_folder="template")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    location = request.form['location']
    balcony = int(request.form['balcony'])
    total_sqft = float(request.form['total_sqft'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,balcony,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# if __name__ == "__main__":
util.load_saved_artifacts()
app.run(host="0.0.0.0", port=5317)