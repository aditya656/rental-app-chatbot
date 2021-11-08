from flask import Flask, jsonify, request
import time

app = Flask(__name__)
# @app.route("/bot",method=["POST"])
@app.route("/",method=["POST"])

def hello():
    return 'Hello World'
#response
# def response():
#     query  = dict(request.form)['query']
#     result = 'pewdiepie'
#     return jsonify({"response":result})

if __name__ == "__main__":
    app.run()
#     app.run(host="0.0.0.0")

