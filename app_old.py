from flask import Flask  # import a class from package

app = Flask(__name__) # create an object

@app.route('/')   # http://www.google.com/
def home():
   return "Hello world!"

app.run(port=5000)

