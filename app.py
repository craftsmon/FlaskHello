from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
   return "Hello world"
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
   return "Hello flask, %s" % name


if __name__ == '__main__':
   app.run(debug=True)