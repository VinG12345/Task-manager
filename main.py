# ==============================
# Часть 1. Менеджер задач
# ==============================

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_done = False  # статус: False = не выполнено, True = выполнено

    def mark_done(self):
        """Отметить задачу как выполненную"""
        self.is_done = True

