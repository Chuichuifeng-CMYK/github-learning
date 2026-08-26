tasks = []

while True:
    print("\n1. 添加任务")
    print("2. 查看任务")
    print("3. 退出")

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
        print("程序结束。")
        break

    else:
        print("请输入 1、2 或 3。")