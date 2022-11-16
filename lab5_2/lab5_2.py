"""
Задание для продвинутых студентов: написать программу генерации файла топологических ограничений для ПЛИС с
использованием шаблона. Шаблон представлен в файле «instants_to_lock.txt». В данном файле ставится в соответствие
положение элемента памяти относительно координат примитивов: горизонтального направления X и вертикального Y. В ПЛИС
18 столбцов встроенной памяти (X – от 0 до 17) и 96 строк (Y – от  0 до 96). Число функциональных узлов CASCAD_much –
от 0 до 1727. Сгенерировать такую последовательность функциональных узлов, для которой каждый соседний узел
(индекс которого отличается на 1) был расположен в соседних координатах вычислительного поля ПЛИС. Результат работы
программы вывести в файл
"""


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
        generateLines(file.readline(), 18, 96)
        file.close()
    except FileNotFoundError:
        print("файл с форматом не найден.")


if __name__ == "__main__":
    main()
