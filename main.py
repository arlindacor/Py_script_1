class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def view_tasks(self):
        if not self.tasks:
            print('Your to-do list is empty.')
        else:
            print('Your to-do list:')
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" completed and removed from the to-do list.')
        else:
            print('Invalid task index.')

# Example usage:
todo_list = ToDoList()

todo_list.add_task("Study Python basics")
todo_list.add_task("Complete coding exercise")
todo_list.view_tasks()

todo_list.complete_task(1)
todo_list.view_tasks()
