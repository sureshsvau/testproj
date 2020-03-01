from flask import Flask, jsonify, request  # import a class from package
app = Flask(__name__) # create an object
app.config['JSON_SORT_KEYS'] = False
import os

@app.route('/')   # http://www.google.com/
def home():
   return "Hello world! Nihal"


@app.route('/Info')
def get_details():
   return jsonify({'service_name':app.name, 'version':os.environ['FLASK_APP_VERSION'], 'git_commit_sha': "abc57858585", 'environment': {'service_port':os.environ['FLASK_RUN_PORT'], 'log_level': "INFO"}})


