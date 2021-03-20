#Nome: Renan A. M. Carvalho
# Dados importados pelo para db mongo via shell: --host=127.0.0.1:27017 -d covid -c iso_code --type csv --file coviddata.csv --headerline

import json

from bson import ObjectId
from flask import flask, request
from pymongo import MongoClient

app = flask(__name__)

client = MongoClient()
db = client.getdatabase ('covid')
collection = db.get_collection('iso_code')

#Faltou o validador
@app.route('/iso_code/create' , methods=['POST'])
def create():
    object_id = collection.insert(request.json)
    return str(object_id)

@app.route('/iso_code/retrive' , methods=['GET'])
def retrive():
    filters = request.args.to_dict(flat=True)
    results = list(collection.find(filters))
    return json.dumps(
        results,
        default=lambda v: str(v) if isinstance(v,ObjectId) else v
        )

@app.route('/iso_code/update/<location>/' , methods=['PATCH'])
def update(location):
    collection.update(
        {'_location': ObjectId(location)},
        {'$set': request.json}
        )
    return id

@app.route('/iso_code/update/<population>/' , methods=['PATCH'])
def update(population):
    collection.update(
        {'_population': ObjectId(population)},
        {'$set': request.json}
        )
    return population


@app.route('/iso_code/delete/<date>/' , methods=['DELETE'])
def delete():
    collection.remove({'_date': ObjectId(date)})
    return date
