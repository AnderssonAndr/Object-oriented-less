from datetime import datetime

class Task():

    tasks_list = []
    def __init__(self, task_to_do, deadline):
        self.task_to_do = task_to_do
        self.deadline = deadline 
        self.done = False
        Task.tasks_list.append(self)
    def mark_done(self):
        self.done = True

    @classmethod
    def add_task(cls, task_to_do, deadline):
        return cls(task_to_do, deadline)
    @classmethod
    def show_current_tasks(cls):
        print("Не выполненные задачи:")
        for idx, task in enumerate(cls.tasks_list, 1):
            if not task.done:
                print(f"{idx}. {task.task_to_do} (Срок до {task.deadline})")
    
task1=Task.add_task("Купить хлеб", "2024-06-20")
task2=Task.add_task("Забрать заказ", "2024-06-21")
task3=Task.add_task("Составить план", "2025-07-04")
Task.show_current_tasks()
task2.mark_done()
Task.show_current_tasks()