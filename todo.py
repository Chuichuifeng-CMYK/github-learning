tasks = []

while True:
    print("\n1. 添加任务")
    print("2. 查看任务")
    print("3. 删除任务")
    print("4. 退出")

    choice = input("请选择：")

    if choice == "1":
        task = input("请输入任务：")
        if task:
            tasks.append(task)
            print("任务已添加。")

    elif choice == "2":
        if not tasks:
            print("目前没有任务。")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        if not tasks:
            print("目前没有任务。")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            number = input("请输入要删除的任务编号：")
            if number.isdigit() and 1 <= int(number) <= len(tasks):
                deleted_task = tasks.pop(int(number) - 1)
                print(f"已删除：{deleted_task}")
            else:
                print("编号无效。")

    elif choice == "4":
        print("程序结束。")
        break

    else:
        print("请输入 1、2、3 或 4。")