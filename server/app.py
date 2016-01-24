from flask import Flask, Response, json, request

app = Flask(__name__)


@app.route('/')
def home():
  return 'Hello, World!'


@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
  dataGet = {
    'message': 'Welcome to Epilog!'
  }


  dataPost = {
    'message': 'Posting to Epilog!'
  }

  if request.method == 'POST':
    js = json.dumps(dataPost)
    response = Response(js, status = 201, mimetype='application/json')

  elif request.method == 'GET':
    js = json.dumps(dataGet)
    response = Response(js, status = 200, mimetype='application/json')

  return response


if __name__ == '__main__':
  app.run(debug = True)
