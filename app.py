import flask
from flask import render_template,Flask

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    return(render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True)