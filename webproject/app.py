from flask import Flask,jsonify,request,make_response,url_for,redirect
import Calculator

import requests,json

app = Flask(__name__)


from flask import request



@app.route('/calculator/', methods=['POST'])
def calculator():
    print "test1"
#    if not request.json or not 'prefixExpression' in request.json:
#        abort(400)
    if request.json.get('prefixExpression'):
        expression = request.json['prefixExpression']
        print expression
        result = Calculator.Calc().prefixEvaluator(expression)

    if request.json.get('infixExpression'):
        expression = request.json['infixExpression']
        result = Calculator.Calc().infixEvaluator(expression)

   # return "hiiii"
#	return json.dumps({'scs': 'scds'})
#	return jsonify({'result': 'hi'}), 201
#    result = Calculator.PrefixCalc().prefixEvaluator(expression)
    print str(result)
    #return str(result)
    return jsonify({'response': str(result)}), 201




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
