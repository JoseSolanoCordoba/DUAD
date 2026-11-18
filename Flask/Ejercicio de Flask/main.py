from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)

WORKING_PATH = Path.cwd()
VALID_STATES = ("pending", "in progress", "completed")

class ItemNotFound(Exception):
    pass

@app.route("/tasks", methods = ["POST"])
def create_task():
    try:
        tasks, file_path = open_json_file()

        if "identifier" not in request.json:
            raise ValueError("identifier missing from the body")
        if verify_identifier_existence(tasks, request.json["identifier"]):
            raise ValueError("identifier repeated")

        if "title" not in request.json:
            raise ValueError("title missing from the body")
        if "description" not in request.json:
            raise ValueError("description missing from the body")
        
        if "state" not in request.json:
            raise ValueError("state missing from the body")
        state = request.json.get("state")
        if state not in VALID_STATES:
            raise ValueError(f'Error: {state} is not a valid state, use {VALID_STATES} instead')
        
        add_tasks_to_json_file(tasks, file_path, request.json)
        
        return jsonify(request.json), 201
    except ValueError as vex:
        return jsonify(message = str(vex)), 400

@app.route("/tasks", methods = ["GET"])
def get_tasks():
    try:
        tasks, file_path = open_json_file()
        state = request.args.get('f')
        if state:
            if state not in VALID_STATES:
                raise ValueError(f'Error: {state} is not a valid state, use {VALID_STATES} instead')
            tasks = filter_tasks(tasks, state)
            if not tasks:
                raise ItemNotFound("Tasks with the desire state were not found")

        return jsonify(tasks), 200
    except ValueError as vex:
        return jsonify(message = str(vex)), 400
    except ItemNotFound as iex:
        return jsonify(message = str(iex)), 404

@app.route("/tasks/<identifier>", methods = ["PATCH"])
def update_tasks(identifier):
    try:
        tasks, file_path = open_json_file()
        title = request.json.get("title")
        description = request.json.get("description")
        state = request.json.get("state")
        if state and state not in VALID_STATES:
            raise ValueError(f'Error: {state} is not a valid state, use {VALID_STATES} instead')
        if not title and not description and not state:
            raise ValueError("Body is empty")
        identifier = int(identifier)
        tasks, item_found = patch_task(tasks, title, description, state, identifier)

        if not item_found:
            raise ItemNotFound("Task to modify does not exist, enter a valid task id")
        
        add_tasks_to_json_file(tasks, file_path)
        return jsonify(tasks), 200
    except ValueError as vex:
        return jsonify(message = str(vex)), 400
    except ItemNotFound as iex:
        return jsonify(message = str(iex)), 404


@app.route("/tasks/<identifier>", methods = ["DELETE"])
def delete_tasks(identifier):
    try:
        tasks, file_path = open_json_file()
        identifier = int(identifier)
        tasks, item_found = delete_task(tasks, identifier)

        if not item_found:
            raise ItemNotFound("Task to delete does not exist, enter a valid task")
        
        add_tasks_to_json_file(tasks, file_path)
        return jsonify({"tasks": tasks, "message": "Remaining tasks after deletion"}), 200
    except ValueError as vex:
        return jsonify(message = str(vex)), 400
    except ItemNotFound as iex:
            return jsonify(message = str(iex)), 404

def open_json_file():
    file_path = WORKING_PATH / "task.json"
    # 1. Read existing tasks if the file already exists
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as json_file:
            try:
                tasks = json.load(json_file)
                # Ensure the loaded data is actually a list
                if not isinstance(tasks, list):
                    tasks = [tasks]
            except json.JSONDecodeError:
                # Handles the case where the file exists but is empty
                tasks = []
    else:
        tasks = []
    return tasks, file_path

def verify_identifier_existence(tasks, identifier):
    identifiers = [task["identifier"] for task in tasks]
    if identifier in identifiers:
        return True
    
def add_tasks_to_json_file (tasks, file_path, new_task_to_add = ''):
    # 2. Append the new JSON object to the list
    if new_task_to_add:
        tasks.append(new_task_to_add)        
    # 3. Write the updated list back to the file
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(tasks, json_file, indent=4)

def filter_tasks (tasks, state):
    filtered_tasks = []
    for task in tasks:
        if task["state"] == state:
            filtered_tasks.append(task)
    return filtered_tasks

def patch_task (tasks, title, description, state, identifier):
    item_found = False
    for task in tasks:
        if task.get("identifier") == identifier:
            if title:
                task["title"] = title
                item_found = True
            if description:
                task["description"] = description
                item_found = True
            if state:
                task["state"] = state
                item_found = True
            break
    return tasks, item_found

def delete_task (tasks, identifier):
    item_found = False
    for index, task in enumerate(tasks):
        if task.get("identifier") == identifier:
            del tasks[index]
            item_found = True
            break
    return tasks, item_found

if __name__ =="__main__":
    app.run(host="localhost", debug = True)