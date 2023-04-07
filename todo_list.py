class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, index, task):
        self.tasks[index] = task

    def remove_task(self, index):
        del self.tasks[index]