import flask
from flask import render_template,Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
@app.route("/",methods=['GET'])
@cross_origin()
def index():
    return(render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True)