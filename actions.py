import os
import shutil
from settings import WORK_DIR

ROOT_DIR = os.path.abspath(WORK_DIR)

if not os.path.exists(ROOT_DIR):
    os.makedirs(ROOT_DIR)


def check_path(current_dir, name):
    target = os.path.abspath(os.path.join(current_dir, name))
    try:
        if os.path.commonpath([ROOT_DIR, target]) == ROOT_DIR:
            return target
    except ValueError:
        return None
    return None


def get_short_path(current_dir):
    rel = os.path.relpath(current_dir, ROOT_DIR)
    if rel == ".":
        return "/"
    return "/" + rel.replace("\\", "/")


def show_dir(current_dir):
    items = os.listdir(current_dir)
    if not items:
        print("Папка пуста.")
        return
    for item in sorted(items):
        full_path = os.path.join(current_dir, item)
        if os.path.isdir(full_path):
            print(f"[Папка] {item}")
        else:
            print(f"        {item}")


def new_dir(current_dir, name):
    path = check_path(current_dir, name)
    if path is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if os.path.exists(path):
        print("Такая папка или файл уже существует.")
        return
    os.makedirs(path)
    print(f"Папка '{name}' создана.")


def del_dir(current_dir, name):
    path = check_path(current_dir, name)
    if path is None or path == ROOT_DIR or path == current_dir:
        print("Ошибка: нельзя удалить эту папку.")
        return
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Папка '{name}' удалена.")
    else:
        print("Такой папки не найдено.")


def go_to_dir(current_dir, name):
    path = check_path(current_dir, name)
    if path is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return current_dir
    if os.path.isdir(path):
        return path
    print("Такой папки не найдено.")
    return current_dir


def go_up(current_dir):
    if current_dir == ROOT_DIR:
        print("Вы уже в корневой папке.")
        return current_dir
    return os.path.dirname(current_dir)
