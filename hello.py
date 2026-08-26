def greet(name):
    name = name.strip()

    if name.lower() == "q":
        return "程序结束。"
    if name:
        return f"你好，{name}！"
    return "你好，学习者！"


def main():
    while True:
        name = input("请输入名字（输入 q 退出）：")
        print(greet(name))

        if name.strip().lower() == "q":
            break


if __name__ == "__main__":
    main()
    print(f"你好，{name}！）