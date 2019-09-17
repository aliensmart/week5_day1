from app import Account
from flask import Flask, jsonify
import os


DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'tteller.db')
Account.dbpath = DBPATH

app = Flask(__name__)

@app.route('/api/account_info/<api_key>', methods=['GET'])
def accoun_info(api_key):
    
    account = Account.api_authenticate(api_key)
    
    data = {}
    
    data["balance"] = account.balance
    data["username"] = account.username

    return jsonify(data)



if __name__=="__main__":
    app.run(debug=True)