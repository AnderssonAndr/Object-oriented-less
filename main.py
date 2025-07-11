from datetime import datetime
class Task():
    tasks = []
    def __init__(self, task_description, deadline, done, not_done):
        self.task_description = task_description
        self.deadline = deadline #строка
        self.done = done
        done = False
        self.not_done = not_done
    Task.tasks.append(self)


    
