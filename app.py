from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/pagecon', methods=['GET'])
def pagecon():
    print(f"Access from {request.remote_addr}, query: {request.args}")
    return "<h2>決済完了</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

