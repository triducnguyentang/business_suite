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
        return []

    def _save_tasks(self):
        # TODO: Implement this method.
        pass

    def _get_next_id(self) -> int:
        # TODO: Implement this method.
        return 1

    def add_task(self, description: str, priority: str, due_date_str: str) -> Task:
        # TODO: Implement this method.
        pass

    def get_all_tasks(self) -> List[Task]:
        # TODO: Implement this method.
        return self.tasks

    def mark_task_complete(self, task_id: int) -> bool:
        # TODO: Implement this method.
        return False

    def delete_task(self, task_id: int) -> bool:
        # TODO: Implement this method.
        return False