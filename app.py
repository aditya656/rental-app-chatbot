# from flask import Flask, jsonify, request
from flask import Flask

app = Flask(__name__)
# @app.route("/bot",method=["POST"])
@app.route('/')
def hello():
    return 'Hello World'
#response
# def response():
#     query  = dict(request.form)['query']
#     result = 'pewdiepie'
#     return jsonify({"response":result})

if __name__ == '__main__':
    app.run()
#     app.run(host="0.0.0.0")

