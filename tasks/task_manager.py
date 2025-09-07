import json
from datetime import datetime
from typing import List, Optional
from .task import Task # <-- Note the updated relative import

class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self, filename: str):
        self.filename = filename
        self.tasks: List[Task] = self._load_tasks()

    def _load_tasks(self) -> List[Task]:
        # TODO: Implement this method.
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                tasks = [Task(**item) for item in data]
                return tasks
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _save_tasks(self):
        # TODO: Implement this method.
        try:
            with open(self.filename, 'w') as file:
                json.dump([task.__dict__ for task in self.tasks], file, indent=4)
        except IOError as e:
            print(f"Error saving tasks to {self.filename}: {e}")
        pass

    def _get_next_id(self) -> int:
        # TODO: Implement this method.
        if self.tasks:
            return max(task.id for task in self.tasks) + 1
        return 1

    def add_task(self, description: str, priority: str, due_date_str: str) -> Task:
        # TODO: Implement this method.
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        new_task = Task(
            id=self._get_next_id(),
            description=description,
            priority=priority,
            due_date=due_date,
            completed=False
        )
        pass

    def get_all_tasks(self) -> List[Task]:
        # TODO: Implement this method.
        for task in self.tasks:
            print(task)
        return self.tasks

    def mark_task_complete(self, task_id: int) -> bool:
        # TODO: Implement this method.
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self._save_tasks()
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        # TODO: Implement this method.
        for i, task in enumerate (self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self._save_tasks()
                return True
        return False