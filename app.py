from flask import Flask, jsonify,request
import time
app = Flask(__name__);
@app.route("/bot", methods=["POST"])
def response():

    query = dict(request.form)['query']
    res = 'Sorry, I cant understand that 😕'
    options = ['Thanks!\nHere is the list of previous orders you have placed.Type Any one order number to get details\n\nID:2736 Camera($45*3Days)\nID:2785 Bike($50*7Days)SunGlasses($2*7Days),'
    ,'Thanks!2','Thanks!3','Thanks!4']
    if 'Hi' in query or 'hi' in query:
        res = 'Hello!!!\n\nWhat can I help you with?\n1.Previous Orders\n2.Tracking Order\n3.Complaints\n4.Call Customer Support'
        return jsonify({"response" : res})
    else:
        try:
            int(query)
            return jsonify({"response" : options[int(query)-1]})
        except:
            return jsonify({"response" : res})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
