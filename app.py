from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/bot",method=["POST"])


#response
def response():
    result = 'pewdiepie'
    return jsonify({"response":result})

if __name__ == '__main__':
    app.run()

