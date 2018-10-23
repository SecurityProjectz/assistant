from flask import Flask,jsonify
from random import randint


app = Flask(__name__)


@app.route('/',methods = ['GET'])
def home():
 return jsonify({'Details':'Lionel Test API'})

@app.route('/stats',methods = ['GET'])
def genRandomStats():
    avg = randint(6,20)
    min = randint(0,10)
    max = randint(20,50)
    count = randint(0,100)
    return jsonify({'avg':avg,'min':min,'max':max,'count':count})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)