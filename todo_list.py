class TodoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 0

    def add_task(self, name):
        self.tasks.append({
            'id': self.task_id_counter,
            'name': name
        })
        self.task_id_counter += 1

    def edit_task(self, task_id, new_name):
        for task in self.tasks:
            if task['id'] == task_id:
                task['name'] = new_name
                break

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]