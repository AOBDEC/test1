from flask import Flask, request
app = Flask(__name__)

@app.route('/pagecon', methods=['GET'])
def pagecon():
    print(f"Access from {request.remote_addr}, query: {request.args}")
    return "<h2>決済完了</h2>"

if __name__ == '__main__':
    app.run()
