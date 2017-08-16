#all the imports
import os
from flask_pymongo import PyMongo
from flask import Flask, current_app, render_template
from flask import jsonify
from flask import request

app = Flask(__name__, static_url_path='')

app.config['MONGO_DBNAME'] = 'nightlife-coordinate-app'
app.config['MONGO_URI'] = 'mongodb://liuerbaozi2260:zja900530@ds139655.mlab.com:39655/nightlife-coordinate-app'
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_stars():
#   star = mongo.db.test
#   output = []
#   for s in star.find():
#     output.append({'date' : s['date']})
#   return jsonify({'result' : output})
  return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug='True')