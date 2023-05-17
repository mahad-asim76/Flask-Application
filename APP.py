import pandas as pd
from flask_cors import CORS
from flask import Flask, jsonify


app = Flask(__name__)
CORS(app)

@app.route('/')
def btc_time_series_analysis():
    url = 'BTC.csv'
    btc_forecast = pd.read_csv(url)
    response = jsonify(btc_forecast.to_dict(orient='records'))
    print(response)
    return response

@app.route('/eth')
def eth_time_series_analysis():
    url = 'ETH.csv'
    eth_forecast = pd.read_csv(url)
    response = jsonify(eth_forecast.to_dict(orient='records'))
    return response

@app.route('/ada')
def ada_time_series_analysis():
    url = 'ADA.csv'
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/dot')
def dot_time_series_analysis():
    url = 'DOT.csv'
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/sol')
def sol_time_series_analysis():
    url = 'SOL.csv'
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/matic')
def matic_time_series_analysis():
    url = 'MATIC.csv'
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

# Run the application
if __name__ == '__main__':
    app.run()
