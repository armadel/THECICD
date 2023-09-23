from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.json.get('task')
        if task:
            tasks.append(task)
            return jsonify({'message': 'Task added successfully'})
        else:
            return jsonify({'error': 'Task cannot be empty'}), 400
    elif request.method == 'GET':
        return jsonify({'tasks': tasks})

if __name__ == '__main__':
    # Change the port to 8080 (or any other desired port)
    app.run(host='0.0.0.0', port=8080)
