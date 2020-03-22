from flask import Flask, jsonify, request, render_template, json
from flask_pymongo import PyMongo
from pymongo import ReturnDocument, MongoClient
from bson import json_util, ObjectId
from config import url
from jsonschema import validate, ValidationError, SchemaError
import jsonschema
import jinja2

app = Flask(__name__)

#config for config variable MONGO_URI (fixed prefix), our mongo DB is in config.py file
app.config["MONGO_URI"] = url

#it tells to use BSON function instead of Flask JSON
json.dumps = json_util.dumps

#linking my flask app with PyMongo and creates the handler 'mongo'
mongo = PyMongo(app)

schema = {
    "type": "object",
    "properties": {
        "Description": {"type": "string"},
        "State": {"type": "string",
                  "minLength": 2,
                  "maxLength": 4
                 },

    },
}

# '@' Python decorator, refers to the same app. app.route takes hello function as a parameter and creates the route for the root '/'
#@app.route('/', defaults={'switch_name': 'How are you?'})
@app.route('/<switch_name>/interfaces.html', methods=["GET"])
def get_interfaces_HTML(switch_name):

    mongo_filter = {"Switch_Type": switch_name}
    #if request.method == "POST":
    #    payload = request.get_json()
    #    if payload is not None:
    #        switch_name = payload.get('description')
    #        return f'Switch name - description, {switch_name}', 200
    #    else:
    #        return f'Error', 400

    #return f'Hello World! I had a {request.method} request from {switch_name}', 200
    #requested_switch_name goes to the template interfaces.html
    result = mongo.db.Interfaces.find(mongo_filter)
    #print(result, "this is", type(result))
    return render_template('interfaces.html', result=result, switch_name=switch_name)

    #return jsonify({'Description': swi})

@app.route('/Switches/interfaces.html', methods=["GET"])
def get_all_interfaces_HTML():

    result = mongo.db.Interfaces.find()
    #print(result, "this is", type(result))
    return render_template('interfaces.html', result=result)

@app.route('/<switch_name>/interfaces.json', methods=["GET"])
def getInterfacesJSON(switch_name):
    #if request.method == "POST":
    #    payload = request.get_json()
    #    if payload is not None:
    #        switch_name = payload.get('description')
    #        return f'Switch name - description, {switch_name}', 200
    #    else:
    #        return f'Error', 400

    mongo_filter = {"Switch_Type": switch_name}
    result = mongo.db.Interfaces.find(mongo_filter)

    return jsonify(result)

@app.route('/Switches/interfaces.json', methods=["GET"])
def getAllInterfacesJSON():

    result = mongo.db.Interfaces.find()

    return jsonify(result)

@app.route('/<switch_name>/<g>/<x>/details.html', methods=["GET"])
def get_interface_xy_detail_HTML(switch_name, g, x):

    interface = 'int ' + g + '/' + x
    mongo_filter = {"Interface_Name": interface}
    #print("mongo filter", mongo_filter)
    result = mongo.db.Interfaces.find(mongo_filter)
    return render_template('details.html', result=result, interface_name=interface)

@app.route('/<switch_name>/<g>/<x>/<y>/details.html', methods=["GET"])
def get_interface_xyz_detail_HTML(switch_name, g, x, y):

    interface = 'int ' + g + '/' + x + '/' + y
    mongo_filter = {"Interface_Name": interface}
    result = mongo.db.Interfaces.find(mongo_filter)
    return render_template('details.html', result=result, interface_name=interface)

@app.route('/<switch_name>/<g>/<x>/interfaces.json', methods=["GET"])
def getInterfaces_xy_detail_JSON(switch_name, g, x):

    interface = 'int ' + g + '/' + x
    mongo_filter = {"Interface_Name": interface}
    result = mongo.db.Interfaces.find(mongo_filter)
    return jsonify(result)

@app.route('/<switch_name>/<g>/<x>/<y>/interfaces.json', methods=["GET"])
def get_interface_xyz_detail_JSON(switch_name, g, x, y):

    interface = 'int ' + g + '/' + x + '/' + y
    mongo_filter = {"Interface_Name": interface}
    result = mongo.db.Interfaces.find(mongo_filter)
    return jsonify(result)

@app.route('/<switch_name>/<ObjectId:_id>', methods=["GET"])
def get_interface_detail_JSON(switch_name, _id):
    mongo_filter = {"_id": _id}
    return mongo_filter
    result = mongo.db.Interfaces.find(mongo_filter)
    return jsonify(result)

@app.route('/<switch_name>/<ObjectId:_id>', methods=["PATCH"])
def patch_interface_description(switch_name, _id):
    #mongo_filter = {"_id": ObjectId(_id)}
    #return mongo_filter

    payload = request.get_json()

    #return schema
    try:
        validate(instance=payload, schema=schema)
    except jsonschema.ValidationError as e:
        print(e.message)
        return "Please insert correct payload!"+" "+e.message, 500
    except jsonschema.SchemaError as e:
        print(e)
        return "Please insert correct payload!"+" "+e, 500
    #return payload
    if payload:
        result = mongo.db.Interfaces.find_one_and_update(

            {"_id": _id},
            {"$set": payload},
            return_document=ReturnDocument.AFTER
        )
        return jsonify(result), 200
    return "Error!", 500


if __name__ == '__main__' :
    app.run(debug = True)