import json
from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data for my todo list
items = [
    {"id": 1, "name": "item1", "description": "This is description of item1"},
    {"id": 2, "name": "item2", "description": "This is description of item2"}
]

@app.route("/")
def home():
    return "Welcome to the TODO Flask app."

## GET : get all items
@app.route("/items", methods = ['GET'])
def get_items():
    return jsonify(items)


## GET: get a single item
@app.route("/items/<int:item_id>", methods = ['GET'])
def get_item(item_id):
    item = next(item for item in items if item['id'] == item_id)
    if item is None:
        return jsonify({"message": "Item not found"})
    return jsonify(item)

## POST: Create a new item
@app.route("/items", methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"message": "Request is not valid."})
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json['name'],
        "description" : request.json.get('description', "No description")
    }
    items.append(new_item)
    return jsonify({"message": "Item created successfully.", "item": new_item})

## PUT: Update an item
@app.route("/items/<int:item_id>", methods = ['PUT'])
def update_item(item_id):
    item = next(item for item in items if item['id'] == item_id)
    if item is None:
        return jsonify({"message" : "Error, item not found."})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify({"message": "Item updated successfully.", "item": item})

## DELETE: Delete an item
@app.route("/items/<int:item_id>", methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted successfully."})

if __name__ == "__main__":
    app.run(debug=True)