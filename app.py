### discord bot ###
### /act ###
### -> DB update
### /show ###
### -> DB read

from flask import *
from flask_compress import Compress
import os
import pandas as pd




app = Flask(__name__, template_folder="./templates")
app.secret_key = os.urandom(12)
compress = Compress(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/act', methods=['POST'])
def act():
    tId = request.form['T_ID']
    sId = request.form['S_ID']
    UNIXTIMESTAMP = request.form['UNIXTIMESTAMP']

    
    with open(str(tId)+'.csv', 'a') as f:
        f.write(f'\n{sId},{UNIXTIMESTAMP}')

    print(tId, sId, UNIXTIMESTAMP)
    return {'status':200, 'message':'OK![POST]'}

@app.route('/act_get', methods=['GET'])
def act_get():
    tId = request.args['T_ID']
    sId = request.args['S_ID']
    UNIXTIMESTAMP = request.args['UNIXTIMESTAMP']
    print(tId, sId, UNIXTIMESTAMP)
    return {'status':200, 'message':'OK![GET]'}

@app.route('/show', methods=['POST'])
def show():
    tId = request.form['T_ID']
    df = pd.read_csv(str(tId)+'.csv')
    return {'status':200, 'message':'OK![POST]', 'data':df.to_dict()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)