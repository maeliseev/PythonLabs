def generateLines(line, x, y):
    try:
        file = open("example_xdc.txt", "w", encoding="utf-8")
        index = 0
        for i in range(x):
            for j in range(y):
                file.write(line.replace("X*", f"X{i}").replace("Y*", f"Y{j}").replace("[*]", f"[{index}]"))
                index += 1

    except FileNotFoundError:
        print("Файл не найден")


def main():
    try:
        file = open("instants_to_lock.txt", "r", encoding="utf-8")
        line = file.readline()
        generateLines(line, 18, 96)
    except FileNotFoundError:
        print("файл с форматом не найден.")


if __name__ == "__main__":
    main()
