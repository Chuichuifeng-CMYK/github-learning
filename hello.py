while True:
    name = input("请输入名字（输入 q 退出）：")

    if name.lower() == "q":
        print("程序结束。")
        break

    if name:
        print(f"你好，{name}！")
    else:
        print("你好，学习者！")