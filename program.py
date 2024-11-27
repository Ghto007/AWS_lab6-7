class Child:
    def set_info(self, last_name, first_name, middle_name, grade):
        """Встановлення інформації про дитину."""
        self.last_name = last_name  # Прізвище дитини
        self.first_name = first_name  # Ім'я дитини
        self.middle_name = middle_name  # По-батькові дитини
        self.grade = grade  # Клас дитини

    def is_equal(self, other):
        """Перевіряє, чи однакові ПІБ двох дітей."""
        return (self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.middle_name == other.middle_name)

    def full_name(self):
        """Повертає повне ім'я дитини."""
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class ClassManager:
    def initialize(self):
        """Ініціалізує порожні списки для черги та видалених дітей."""
        self.children_queue = []  # Черга дітей
        self.deleted_children = []  # Список видалених дітей

    def add_child(self, last_name, first_name, middle_name, grade):
        """Додає дитину до черги."""
        child = Child()
        child.set_info(last_name, first_name, middle_name, grade)

        # Перевіряємо, чи така дитина вже є у списку
        if not any(c.is_equal(child) for c in self.children_queue):
            self.children_queue.append(child)  # Додаємо дитину до черги
            self.children_queue.sort(key=lambda x: (x.grade, x.last_name, x.first_name, x.middle_name))  # Сортуємо спочатку за класом, потім за алфавітом
            print(f"Дитина '{child.full_name()}' додана до класу {grade}.")
        else:
            print(f"Дитина з ПІБ '{child.full_name()}' вже існує.")

    def get_children_by_grade(self, grade):
        """Отримати всіх дітей у вказаному класі."""
        children_in_grade = [child for child in self.children_queue if child.grade == grade]
        return children_in_grade

    def delete_child_by_index(self, grade, index):
        """Видалити дитину по індексу зі списку."""
        children_in_grade = self.get_children_by_grade(grade)
        if 0 <= index < len(children_in_grade):
            child_to_remove = children_in_grade[index]
            self.children_queue.remove(child_to_remove)  # Видаляємо дитину зі списку
            self.deleted_children.append(child_to_remove)  # Додаємо дитину до списку видалених
            print(f"Дитину '{child_to_remove.full_name()}' видалено з класу {grade}.")
        else:
            raise IndexError("Невірний індекс.")  # Викидаємо IndexError

    def edit_child_by_index(self, grade, index, new_last_name, new_first_name, new_middle_name):
        """Редагувати інформацію про дитину по індексу."""
        children_in_grade = self.get_children_by_grade(grade)
        if 0 <= index < len(children_in_grade):
            child_to_edit = children_in_grade[index]
            self.children_queue.remove(child_to_edit)  # Видаляємо стару дитину
            # Оновлюємо інформацію про дитину
            child_to_edit.set_info(new_last_name, new_first_name, new_middle_name, grade)
            self.children_queue.append(child_to_edit)  # Додаємо дитину з новою інформацією
            self.children_queue.sort(key=lambda x: (x.grade, x.last_name, x.first_name, x.middle_name))  # Сортуємо спочатку за класом, потім за алфавітом
            print(f"Дані дитини в класі {grade} змінено.")
        else:
            raise IndexError("Невірний індекс.")  # Викидаємо IndexError

    def display_children_in_grade(self, grade):
        """Відображає дітей у вказаному класі."""
        children_in_grade = self.get_children_by_grade(grade)
        # Сортуємо перед відображенням, щоб забезпечити правильний порядок
        children_in_grade.sort(key=lambda x: (x.last_name, x.first_name, x.middle_name))
        if children_in_grade:
            print(f"Діти в класі {grade}:")
            for i, child in enumerate(children_in_grade):
                print(f"{i + 1}. {child.full_name()}")
        else:
            print(f"Немає дітей у класі {grade}.")

    def add_child(self, last_name, first_name, middle_name, grade):
        """Додає дитину до черги."""
        # Перевірка на None і порожні рядки
        if not last_name or not first_name or not middle_name or not grade:
            raise ValueError("Усі поля повинні бути заповнені.")
        
        child = Child()
        child.set_info(last_name, first_name, middle_name, grade)

        # Перевіряємо, чи така дитина вже є у списку
        if not any(c.is_equal(child) for c in self.children_queue):
            self.children_queue.append(child)  # Додаємо дитину до черги
            self.children_queue.sort(key=lambda x: (x.grade, x.last_name, x.first_name, x.middle_name))  # Сортуємо спочатку за класом, потім за алфавітом
            print(f"Дитина '{child.full_name()}' додана до класу {grade}.")
        else:
            print(f"Дитина з ПІБ '{child.full_name()}' вже існує.")

    def display_all_children(self):
        """Відображає всіх дітей."""
        if self.children_queue:
            print("Список дітей:")
            for child in self.children_queue:
                print(f"- {child.full_name()}, Клас: {child.grade}")
        else:
            print("Немає дітей для відображення.")

    def display_deleted_children(self):
        """Відображає всіх видалених дітей."""
        if self.deleted_children:
            print("Список видалених дітей:")
            for child in self.deleted_children:
                print(f"- {child.full_name()}, Клас: {child.grade}")
        else:
            print("Список видалених дітей порожній.")


# Функція для створення екземпляру ClassManager
def create_class_manager():
    """Створює новий менеджер класу та ініціалізує його."""
    class_manager = ClassManager()
    class_manager.initialize()  # Ініціалізація класу
    return class_manager


# Приклад використання меню
def main_menu():
    """Меню програми для управління класами дітей."""
    class_manager = create_class_manager()

    while True:
        # Виводимо меню користувачу
        print("\nМеню:")
        print("1. Додати дитину")
        print("2. Видалити дитину по класу")
        print("3. Редагувати інформацію про дитину по класу")
        print("4. Показати список дітей")
        print("5. Показати список видалених дітей")
        print("0. Вийти")

        # Отримуємо вибір користувача
        choice = input("Оберіть опцію: ")

        if choice == "1":
            # Додаємо нову дитину
            last_name = input("Введіть прізвище: ")
            first_name = input("Введіть ім'я: ")
            middle_name = input("Введіть по-батькові: ")
            grade = input("Введіть клас (наприклад, '1А'): ")
            class_manager.add_child(last_name, first_name, middle_name, grade)

        elif choice == "2":
            # Видаляємо дитину
            grade = input("Введіть клас для видалення дитини: ")
            class_manager.display_children_in_grade(grade)
            index = int(input("Оберіть номер дитини для видалення: ")) - 1
            try:
                class_manager.delete_child_by_index(grade, index)
            except IndexError as e:
                print(e)

        elif choice == "3":
            # Редагуємо дані про дитину
            grade = input("Введіть клас для редагування дитини: ")
            class_manager.display_children_in_grade(grade)
            index = int(input("Оберіть номер дитини для редагування: ")) - 1
            new_last_name = input("Введіть нове прізвище: ")
            new_first_name = input("Введіть нове ім'я: ")
            new_middle_name = input("Введіть нове по-батькові: ")
            try:
                class_manager.edit_child_by_index(grade, index, new_last_name, new_first_name, new_middle_name)
            except IndexError as e:
                print(e)

        elif choice == "4":
            # Показуємо всіх дітей
            class_manager.display_all_children()

        elif choice == "5":
            # Показуємо видалених дітей
            class_manager.display_deleted_children()

        elif choice == "0":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Запуск програми
if __name__ == "__main__":
    main_menu()
