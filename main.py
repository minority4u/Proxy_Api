import os
from flask import Flask, jsonify, abort, request, make_response, url_for
import box_handler

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))


BOXES = box_handler.Box_Handler().get_boxes()

def abort_if_box_doesnt_exist(box_id):
    if box_id not in BOXES:
        abort(404)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/')
def hello_world():
    return 'Hello World! I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0))

@app.route('/users/')
def return_users():
    return jsonify({'tasks': BOXES})



@app.route('/boxes/')
def return_boxes():
    return jsonify({'boxes': BOXES})

@app.route('/boxes/<int:box_id>')
def return_single_box(box_id):
    abort_if_box_doesnt_exist(box_id)
    return jsonify( { 'Box': BOXES[box_id] } )

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)