from flask import Flask,jsonify,request,make_response,url_for,redirect
import Calculator

import requests,json

app = Flask(__name__)


from flask import request



@app.route('/prefixCalculator/', methods=['POST'])
def create_task():
    print "test1"
#    if not request.json or not 'prefixExpression' in request.json:
#        abort(400)
    expression = request.json['prefixExpression']
    print expression
   # return "hiiii"
#	return json.dumps({'scs': 'scds'})
#	return jsonify({'result': 'hi'}), 201
    result = Calculator.PrefixCalc().prefixEvaluator(expression)
    print str(result)
    #return str(result)
    return jsonify({'prefixResult': str(result)}), 201




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
