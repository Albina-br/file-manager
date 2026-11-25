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

def new_file(current_dir, name):
    path = check_path(current_dir, name)
    if path is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if os.path.exists(path):
        print("Такой файл или папка уже существует.")
        return
    if not os.path.isdir(os.path.dirname(path)):
        print("Указанная папка не найдена.")
        return
    with open(path, "w", encoding="utf-8"):
        pass
    print(f"Файл '{name}' создан.")


def write_file(current_dir, name):
    path = check_path(current_dir, name)
    if path is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if os.path.isdir(path):
        print("Это папка, а не файл.")
        return
    if not os.path.isdir(os.path.dirname(path)):
        print("Папка для файла не найдена.")
        return
    text = input("Введите текст: ")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Текст записан в файл '{name}'.")


def read_file(current_dir, name):
    path = check_path(current_dir, name)
    if path is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            if content:
                print(content, end="")
            else:
                print("(Файл пуст)")
        except UnicodeDecodeError:
            print("Ошибка: файл не является текстовым.")
    else:
        print("Файл не найден.")


def del_file(current_dir, name):
    path = check_path(current_dir, name)
    if path is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if os.path.isfile(path):
        os.remove(path)
        print(f"Файл '{name}' удалён.")
    else:
        print("Файл не найден.")


def copy_file(current_dir, src_name, dst_name):
    src = check_path(current_dir, src_name)
    dst = check_path(current_dir, dst_name)
    if src is None or dst is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if not os.path.isfile(src):
        print("Исходный файл не найден.")
        return
    if not os.path.isdir(dst) and not os.path.isdir(os.path.dirname(dst)):
        print("Папка назначения не найдена.")
        return
    shutil.copy(src, dst)
    print(f"Файл '{src_name}' скопирован в '{dst_name}'.")


def move_file(current_dir, src_name, dst_name):
    src = check_path(current_dir, src_name)
    dst = check_path(current_dir, dst_name)
    if src is None or dst is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if not os.path.isfile(src):
        print("Исходный файл не найден.")
        return
    if not os.path.isdir(dst) and not os.path.isdir(os.path.dirname(dst)):
        print("Папка назначения не найдена.")
        return
    shutil.move(src, dst)
    print(f"Файл '{src_name}' перемещён в '{dst_name}'.")


def ren_file(current_dir, old_name, new_name):
    old_path = check_path(current_dir, old_name)
    new_path = check_path(current_dir, new_name)
    if old_path is None or new_path is None:
        print("Ошибка: нельзя выходить за пределы рабочей папки.")
        return
    if not os.path.isfile(old_path):
        print("Файл не найден.")
        return
    if os.path.exists(new_path):
        print("Файл с таким именем уже существует.")
        return
    if not os.path.isdir(os.path.dirname(new_path)):
        print("Папка назначения не найдена.")
        return
    os.rename(old_path, new_path)
    print(f"Файл '{old_name}' переименован в '{new_name}'.")
