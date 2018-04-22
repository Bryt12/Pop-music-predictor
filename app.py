from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hit", methods=['GET'])
def hit_or_not():
    pass

if __name__='__main__':
    app.run()
