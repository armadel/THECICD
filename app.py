from flask import Flask, request, jsonify
import random

app = Flask(__name__)
tasks = []

def generate_random_task():
    adjectives = ['Complete', 'Create', 'Update', 'Review', 'Finish']
    nouns = ['report', 'project', 'presentation', 'task', 'assignment']
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

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
    # Generate 5 random tasks at startup
    tasks.extend([generate_random_task() for _ in range(5)])

    app.run(host='0.0.0.0', port=8080)
