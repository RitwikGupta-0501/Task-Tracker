from datetime import datetime
import json

# INITIALIZING CODE
with open("Tasks.jsonl", "r") as tasks:
        try:
            LAST_CREATED_TASK = json.loads(list(tasks)[-1])["id"] + 1
            print(LAST_CREATED_TASK)
        except IndexError:
            LAST_CREATED_TASK = 0

class Task:

    TASK_COUNT = LAST_CREATED_TASK

    def __init__(self, desc):
        self.id = Task.TASK_COUNT
        Task.TASK_COUNT += 1
        self.desc = desc
        self.status = "n"
        self.createdAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.updatedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.add()

    def add(self) -> None:
        with open("Tasks.jsonl", "a") as tasks:
            json.dump(self.__dict__, tasks)
            tasks.write('\n')
    
    def update(self, new_desc) -> None:
        with open("Tasks.jsonl", "r") as tasks:
            data = tasks.readlines()
            task = json.loads(data[self.id])
            task["updatedAt"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            task["desc"] = new_desc
            data[self.id] = json.dumps(task) + '\n'
        with open("Tasks.jsonl", "w") as tasks:
            tasks.writelines(data)
    
    def delete(self) -> None:
        with open("Tasks.jsonl", "r") as tasks:
            data = tasks.readlines()
            data.pop(self.id)
        with open("Tasks.jsonl", "w") as tasks:
            tasks.writelines(data)


if __name__ == '__main__':

    Task("Task 1")
    task = Task("Task 2")
    Task("Task 3")
    task.update("Updated Task 2")
    task.delete()
