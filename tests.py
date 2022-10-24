# файл tests.py
import unittest
import os
import delete  # тестируемый модуль


class TestDelete(unittest.TestCase):
    def test_delete_file(self):  # удаление файла
        my_file = open("delete.txt", "w+")  # создаем файлы для удаления
        my_file.write("delete")
        my_file.close()
        self.assertEqual(delete.delete("delete.txt"), True)

    def test_delete_folder(self):  # удаление папки
        os.makedirs("nested1/nested2/nested3")  # создаем папки для удаления
        my_file = open("delete.txt", "w+")
        my_file.write("delete")
        my_file.close()
        os.replace("delete.txt", "nested1/nested2/nested3/delete.txt")  # переносим файл в самый нижний каталог
        self.assertEqual(delete.delete("nested1"), True)

    def test_delete_not_existed_file(self):  # удаление не существующего файла/папки
        self.assertEqual(delete.delete("iregierjgreg"), False)
