from dataclasses import dataclass
from datetime import date

@dataclass
class Task:
    """Represents a single task."""
    task_id: int
    description: str
    priority: str
    due_date: date
    is_complete: bool = False

    def __str__(self) -> str:
        status = "Done" if self.is_complete else "Pending"
        return (f"ID: {self.task_id} | Status: {status} | Due: {self.due_date}\n"
                f"  Priority: {self.priority}\n"
                f"  Description: {self.description}")