from datetime import date

class Task():
    def __init__(self, descr, deadline):
        self.descr = descr
        self.deadline = deadline
        self.status = False

    def set_status(self, status):
        self.status = status

tasks = []

def add_task(descr, deadline):
    task = Task(descr, deadline)
    tasks.append(task)
    return task

def print_tasks():
    print("Список не выполненных задач:")
    for task in tasks:
        if not task.status:
            print(f"{task.descr}, срок {task.deadline}")
    print()

task1 = add_task("Сделать презентацию", date(2025, 6, 25))
task2 = add_task("Закупить материалы", date(2025, 6, 15))
task3 = add_task("Отправить счёт в банк", date(2025, 6, 22))
print_tasks()

task2.set_status(True)
print_tasks()