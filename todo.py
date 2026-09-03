import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todo.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def main():
    tasks = load_tasks()

    while True:
        print("\n1. 添加任务")
        print("2. 查看任务")
        print("3. 删除任务")
        print("4. 退出")

        choice = input("请选择：")

        if choice == "1":
            task = input("请输入任务：")
            tasks.append(task)
            save_tasks(tasks)
            print("任务已添加")

        elif choice == "2":
            if not tasks:
                print("暂无任务")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("暂无任务")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                number = int(input("请输入要删除的编号："))
                tasks.pop(number - 1)
                save_tasks(tasks)
                print("任务已删除")
            except (ValueError, IndexError):
                print("编号无效")

        elif choice == "4":
            print("程序结束")
            break

        else:
            print("选项无效")


if __name__ == "__main__":
    main()