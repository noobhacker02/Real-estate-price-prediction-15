from flask import Flask, request, jsonify
from flask import render_template
import util

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'Locations': util.get_location_names()  
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route("/")
def test():
    return render_template("index.html")


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    Location = request.form['Location']
    Area = float(request.form['Area'])
    bhk = int(request.form['bhk'])
    Lift = int(request.form['Lift'])
    Parking = int(request.form['Parking'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(Location, Area, bhk, Lift,Parking)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)