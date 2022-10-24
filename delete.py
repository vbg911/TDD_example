import os
import shutil

def delete(file_path):
    is_file = isFile(file_path)
    if is_file:
        return delete_file(file_path)

    return False


def isFile(file_path):
    return os.path.isfile(file_path)


def delete_file(file_path):
    with open(file_path, "wb") as f:
        f.write(bytes('qQq', 'utf8'))
        f.close()

    with open(file_path, "wb") as f:
        f.write(bytes('AaA', 'utf8'))
        f.close()

    with open(file_path, "wb") as f:
        f.write(bytes('PpP', 'utf8'))
        f.close()

    os.remove(file_path)
    if os.path.exists(file_path):
        return False
    else:
        return True

if __name__ == '__main__':
    file_path = input("Введите путь к файлу/папке: ")
    delete(file_path)
