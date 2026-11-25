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
