"""
Задание для продвинутых студентов: написать программу генерации файла топологических ограничений для ПЛИС с
использованием шаблона. Шаблон представлен в файле «instants_to_lock.txt». В данном файле ставится в соответствие
положение элемента памяти относительно координат примитивов: горизонтального направления X и вертикального Y. В ПЛИС
18 столбцов встроенной памяти (X – от 0 до 17) и 96 строк (Y – от  0 до 96). Число функциональных узлов CASCAD_much –
от 0 до 1727. Сгенерировать такую последовательность функциональных узлов, для которой каждый соседний узел
(индекс которого отличается на 1) был расположен в соседних координатах вычислительного поля ПЛИС. Результат работы
программы вывести в файл
"""


def generate_lines(line, x, y):
    file = open("example_xdc.txt", "w", encoding="utf-8")
    index = 0

    def write_plus_index(arg1, arg2):
        nonlocal index
        file.write(line.replace("X*", f"X{arg1}").replace("Y*", f"Y{arg2}").replace("[*]", f"[{index}]"))
        index += 1

    for i in range(x):
        for j in range(y):
            if i % 2 == 0:
                write_plus_index(i, j)
            else:
                write_plus_index(i, y - j - 1)


def main():
    try:
        file = open("instants_to_lock.txt", "r", encoding="utf-8")
        generate_lines(file.readline(), 18, 96)
        file.close()
    except FileNotFoundError:
        print("файл с форматом не найден.")


if __name__ == "__main__":
    main()
