from flask import jsonify, request
from .run import app
from ttrade import Account,util

@app.route('/', methods=["GET"])
def root():
    return jsonify({"name":"Terminal Trader API"})

@app.route('/api/price/<ticker>', methods=['GET'])
def get_price(ticker):
    try:
        price = util.get_price(ticker)
    except ConnectionError:
        return jsonify({"error": "could not connect to the market api"}), 500
    
    return jsonify({"ticker":ticker.lower(), "price": price})

@app.route('/api/create', methods=['POST'])
def create_account():
    pass

@app.route('/api/get_api_key', methods=['POST'])
def get_api_key():
    pass

@app.route('/api/<api_key>/balance', methods=['GET'])
def balance(api_key):
    pass

@app.route('/api/<api_key>/positions/<ticker>', methods=['GET'])
def position_for(api_key, ticker):
    pass

@app.route('/api/<api_key>/positions', methods=['GET'])
def all_positions(api_key):
    pass

@app.route('/api/<api_key>/trades', methods=['GET'])
def all_trades(api_key):
    pass

@app.route('/api/<api_key>/trades/<ticker>', methods=['GET'])
def trade_for(api_key, ticker):
    pass

@app.route('/api/<api_key>/deposit', methods=['PUT'])
def deposit(api_key):
    pass

@app.route('/api/<api_key>/buy', methods=['POST'])
def buy(api_key):
    pass

@app.route('/api/<api_key>/sell', methods=['POST'])
def sell(api_key):
    pass

@app.errorhandler(404)
def err_404(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(405)
def err_405(e):
    return jsonify({"error":"method not allowed"})



