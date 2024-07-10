import yfinance as yf
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json().get('ticker')
    if not ticker:
        return jsonify({'error': 'Ticker symbol is required'}), 400
    data = yf.Ticker(ticker).history(period='1y')
    if data.empty:
        return jsonify({'error': 'Invalid ticker symbol'}), 400
    return jsonify({'currentPrice': data.iloc[-1].Close,
                    'openPrice': data.iloc[-1].Open})

@app.route('/get_stock_data', methods=['GET'])
def handle_get_request():
    return jsonify({'message': 'Send a POST request with JSON data including a "ticker" key.'})

if __name__ == '__main__':
    app.run(debug=True)
