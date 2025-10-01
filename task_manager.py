class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.done = False  # статус: выполнено или нет

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✔️ Выполнено" if self.done else "✘ Не выполнено"
        return f"{self.description} (срок: {self.deadline}) — {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()

    def show_current_tasks(self):
        print("Текущие задачи:")
        for i, task in enumerate(self.tasks):
            if not task.done:
                print(f"{i}. {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Сделать уроки", "2024-06-15")
    manager.add_task("Купить продукты", "2024-06-14")
    manager.add_task("Позвонить другу", "2024-06-16")

    manager.show_current_tasks()

    # Отмечаем задачу выполненной
    manager.mark_task_done(1)

    print("\nПосле обновления:")
    manager.show_current_tasks()
