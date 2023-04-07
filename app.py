from flask import Flask, render_template, request, redirect, url_for
from todo_list import ToDOList

app = Flask(__name__)
todo_list = ToDOList()

@app.route('/')
def index():
    return render_template("index.html", task=todo_list.tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todo_list.add_task(task)
    return redirect(url_for('index'))

@app.route('/edit_task/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    if request.method == 'POST':
        task = request.form['task']
        todo_list.edit_task(task_id, task)
        return redirect(url_for('index'))
    else:
        return render_template("edit_task.html", task=todo_list.tasks[index], index=index)

@app.route("/remove_task/<int:index>")
def remove_task(index):
    todo_list.remove_task(index)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)