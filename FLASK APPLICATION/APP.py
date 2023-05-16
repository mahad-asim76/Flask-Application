import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
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
    file_id = '1yjhPB5a-xRXXlokKRzkjMCltA02SxMZk'
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(url)
    btc_forecast = pd.read_csv(url)
    response = jsonify(btc_forecast.to_dict(orient='records'))
    print(response)
    return response

@app.route('/api/eth')
def eth_time_series_analysis():
    url = 'ETH.csv'
    file_id = '1U1tDHhurrDX_QcBm6h4XBGjh0HiDkhR3'
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(url)
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
    file_id = '1wtLJVHCOsFdnoAX3rWiAY6jQXsBVHqAE'
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(url)
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/api/sol')
def sol_time_series_analysis():
    url = 'SOL.csv'
    file_id = '1Cu36TwbdPMjDxPmcXyWo2sZ5hJgDkhXC'
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(url)
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

@app.route('/api/matic')
def matic_time_series_analysis():
    url = 'MATIC.csv'
    file_id = '19dqp6GH6FqTgSYWC02aS4pVPGFMGBBTc'
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(url)
    ada_forecast = pd.read_csv(url)
    response = jsonify(ada_forecast.to_dict(orient='records'))
    return response

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')