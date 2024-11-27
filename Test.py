import unittest
import sys
from program import Child, ClassManager
from io import StringIO

class TestChild(unittest.TestCase):

    def test_full_name(self):
        child = Child()
        child.set_info("Іванов", "Іван", "Іванович", "2А")
        self.assertEqual(child.full_name(), "Іванов Іван Іванович")

    def test_is_equal(self):
        child1 = Child()
        child1.set_info("Петренко", "Олег", "Олегович", "3Б")
        child2 = Child()
        child2.set_info("Петренко", "Олег", "Олегович", "3Б")
        child3 = Child()
        child3.set_info("Сидоренко", "Григорій", "Григорович", "3Б")
        
        self.assertTrue(child1.is_equal(child2))
        self.assertFalse(child1.is_equal(child3))


class TestClassManager(unittest.TestCase):

    def setUp(self):
        """Створює новий менеджер класу перед кожним тестом."""
        self.manager = ClassManager()
        self.manager.initialize()

    def test_add_child(self):
        self.manager.add_child("Іванов", "Іван", "Іванович", "1А")
        self.assertEqual(len(self.manager.children_queue), 1)

    def test_add_duplicate_child(self):
        self.manager.add_child("Іванов", "Іван", "Іванович", "1А")
        self.manager.add_child("Іванов", "Іван", "Іванович", "1А")  # Дубль
        self.assertEqual(len(self.manager.children_queue), 1)

    def test_delete_child(self):
        self.manager.add_child("Петренко", "Олег", "Олегович", "2Б")
        self.manager.delete_child_by_index("2Б", 0)
        self.assertEqual(len(self.manager.children_queue), 0)
        self.assertEqual(len(self.manager.deleted_children), 1)

    def test_delete_child_invalid_index(self):
        self.manager.add_child("Сидоренко", "Григорій", "Григорович", "3А")
        with self.assertRaises(IndexError):
            self.manager.delete_child_by_index("3А", 1)

    def test_edit_child(self):
        self.manager.add_child("Коваленко", "Сергій", "Сергійович", "1В")
        self.manager.edit_child_by_index("1В", 0, "Коваленко", "Сергій", "Іванович")
        self.assertEqual(self.manager.children_queue[0].middle_name, "Іванович")

    def test_edit_child_invalid_index(self):
        self.manager.add_child("Гуменюк", "Леонід", "Леонідович", "4А")
        with self.assertRaises(IndexError):
            self.manager.edit_child_by_index("4А", 1, "Гуменюк", "Леонід", "Петрович")

    def test_get_children_by_grade(self):
        self.manager.add_child("Шевченко", "Тарас", "Григорович", "5А")
        self.manager.add_child("Петренко", "Іван", "Сергійович", "5А")
        children = self.manager.get_children_by_grade("5А")
        self.assertEqual(len(children), 2)

    def test_display_children_in_grade(self):
        self.manager.add_child("Тимошенко", "Анастасія", "Леонідівна", "6А")
        self.manager.display_children_in_grade("6А")  # Вивід на екран, не перевіряємо


    def test_add_child_invalid_data(self):
        with self.assertRaises(ValueError):
            self.manager.add_child(None, "Іван", "Іванович", "2А")  # Перевірка на None
        with self.assertRaises(ValueError):
            self.manager.add_child("", "Іван", "Іванович", "2А")  # Перевірка на пустий рядок
        with self.assertRaises(ValueError):
            self.manager.add_child("Іванов", "", "Іванович", "2А")  # Перевірка на пустий рядок
        with self.assertRaises(ValueError):
            self.manager.add_child("Іванов", "Іван", "", "2А")  # Перевірка на пустий рядок
        with self.assertRaises(ValueError):
            self.manager.add_child("Іванов", "Іван", "Іванович", "")  # Перевірка на пустий рядок



    def test_delete_child_no_children(self):
        with self.assertRaises(IndexError):
            self.manager.delete_child_by_index("1А", 0)  # Видалення з порожнього списку

    def test_edit_child_no_children(self):
        with self.assertRaises(IndexError):
            self.manager.edit_child_by_index("1А", 0, "Новий", "Ім'я", "По-батькові")  # Редагування з порожнього списку


# Запуск тестів
if __name__ == '__main__':
    unittest.main(verbosity=1)

