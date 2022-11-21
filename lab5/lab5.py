"""
8. Написать программу, которая подсчитывает общее число символов в тексте, без учета спецсимволов и знаков препинания.
Также необходимо подсчитать число уникальных слов, состоящих из 3х символов. Результат работы программы вывести в файл.
Данные в файле должны быть структурированы и подписаны.
"""
import re


def read_all_file(path):
    try:
        file = open(path, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        return []


def get_count_alpha_char(list_lines):
    char_dictionaries = {}
    for line in list_lines:
        for char in line:
            if not char.isalpha():
                break

            if char_dictionaries.get(char) is None:
                char_dictionaries[char] = 1
            else:
                char_dictionaries[char] += 1

    return char_dictionaries


def get_count_word(list_lines, size_word):
    word_dictionaries = {}
    for line in list_lines:
        for word in re.sub('[,.!?’”]', '', line).split(" "):
            if len(word) != size_word:
                break
            if word_dictionaries.get(word) is None:
                word_dictionaries[word] = 1
            else:
                word_dictionaries[word] += 1

    return word_dictionaries


# будите молодцы, если файла нет, вы его создадите, но мне лень
def main():
    lines = read_all_file("Harry_Potter.txt")

    file = open("laba5.txt", "w", encoding="utf-8")
    file.write(f"{get_count_alpha_char(lines)}\n{get_count_word(lines, 3)}")
    file.close()


if __name__ == "__main__":
    main()
