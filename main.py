import actions


def show_commands():
    print("Доступные команды:")
    print("  show                          - показать содержимое папки")
    print("  new_dir <имя>                 - создать папку")
    print("  del_dir <имя>                 - удалить папку")
    print("  go <имя>                      - зайти в папку")
    print("  up                            - подняться на уровень вверх")
    print("  new_file <имя>                - создать пустой файл")
    print("  write <имя>                   - записать текст в файл")
    print("  read <имя>                    - прочитать текстовый файл")
    print("  del_file <имя>                - удалить файл")
    print("  copy_file <откуда> <куда>     - скопировать файл")
    print("  move_file <откуда> <куда>     - переместить файл")
    print("  ren_file <старое> <новое>     - переименовать файл")
    print("  commands                      - список команд")
    print("  stop                          - выход из программы")


def main():
    current_dir = actions.ROOT_DIR
    print("Файловый менеджер запущен. Введите 'commands' для списка команд.")

    while True:
        short_path = actions.get_short_path(current_dir)
        user_input = input(f"\n[{short_path}] > ").strip()
        if not user_input:
            continue

        parts = user_input.split()
        cmd = parts[0]

        if cmd == "stop":
            print("Работа завершена.")
            break
        elif cmd == "commands":
            show_commands()
        elif cmd == "show":
            actions.show_dir(current_dir)
        elif cmd == "up":
            current_dir = actions.go_up(current_dir)
        elif cmd == "new_dir":
            if len(parts) != 2:
                print("Использование: new_dir <имя>")
            else:
                actions.new_dir(current_dir, parts[1])
        elif cmd == "del_dir":
            if len(parts) != 2:
                print("Использование: del_dir <имя>")
            else:
                actions.del_dir(current_dir, parts[1])
        elif cmd == "go":
            if len(parts) != 2:
                print("Использование: go <имя>")
            else:
                current_dir = actions.go_to_dir(current_dir, parts[1])
        elif cmd == "new_file":
            if len(parts) != 2:
                print("Использование: new_file <имя>")
            else:
                actions.new_file(current_dir, parts[1])
        elif cmd == "write":
            if len(parts) != 2:
                print("Использование: write <имя>")
            else:
                actions.write_file(current_dir, parts[1])
        elif cmd == "read":
            if len(parts) != 2:
                print("Использование: read <имя>")
            else:
                actions.read_file(current_dir, parts[1])
        elif cmd == "del_file":
            if len(parts) != 2:
                print("Использование: del_file <имя>")
            else:
                actions.del_file(current_dir, parts[1])
        elif cmd == "copy_file":
            if len(parts) != 3:
                print("Использование: copy_file <откуда> <куда>")
            else:
                actions.copy_file(current_dir, parts[1], parts[2])
        elif cmd == "move_file":
            if len(parts) != 3:
                print("Использование: move_file <откуда> <куда>")
            else:
                actions.move_file(current_dir, parts[1], parts[2])
        elif cmd == "ren_file":
            if len(parts) != 3:
                print("Использование: ren_file <старое_имя> <новое_имя>")
            else:
                actions.ren_file(current_dir, parts[1], parts[2])
        else:
            print("Неизвестная команда. Введите 'commands' для справки.")


if __name__ == "__main__":
    main()
