import flask
from flask import render_template,Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
@app.route("/atliq",methods=['GET'])
@cross_origin()
def index():
    return('<iframe title="Sales insight" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=4e1312ed-87fa-43bb-ba27-159f86f4fa61&autoAuth=true&ctid=0df4f8da-952d-4c0a-80fa-408c57b08ef6" frameborder="0" allowFullScreen="true"></iframe>')

if __name__ == '__main__':
    app.run(debug=True)