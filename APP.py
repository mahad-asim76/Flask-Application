import pandas as pd
from flask_cors import CORS
from flask import Flask, jsonify

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

app = Flask(__name__)
CORS(app)

@app.route('/api/btc')
def btc_time_series_analysis():
    url = 'BTC.csv'
    btc_forecast = pd.read_csv(url)
    response = jsonify(btc_forecast.to_dict(orient='records'))
    print(response)
    return response

@app.route('/api/eth')
def eth_time_series_analysis():
    url = 'ETH.csv'
    eth_forecast = pd.read_csv(url)
    response = jsonify(eth_forecast.to_dict(orient='records'))
    return response

@app.route('/api/ada')
def ada_time_series_analysis():
    url = 'ADA.csv'
    file_id = '1rZNDKmnyN9rdLbT3DIzAinkGODuzGNjB'
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(url)
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/api/dot')
def dot_time_series_analysis():
    url = 'DOT.csv'
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/api/sol')
def sol_time_series_analysis():
    url = 'SOL.csv'
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/api/matic')
def matic_time_series_analysis():
    url = 'MATIC.csv'
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
