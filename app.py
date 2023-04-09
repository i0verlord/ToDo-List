from flask import Flask, render_template, request, redirect, url_for
from todo_list import ToDoList

app = Flask(__name__)
todo_list = ToDoList()

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list.tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    todo_list.add_task(task_name)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    new_task_name = request.form['new_task_name']
    todo_list.edit_task(task_id, new_task_name)
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>', methods=['POST'])
def remove_task(task_id):
    todo_list.remove_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)