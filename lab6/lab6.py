"""
Вар 7.
Дано: Множество пользователей и наборы сайтов, которые каждый из них посещает часто
Нужно: Список сайтов, которые посещаются наибольшим или наименьшим числом пользователей
"""


class User:
    def __init__(self, user_name, links):
        self.user_name = user_name
        self.links = links


def getPopularLink(users):
    link_count = {}
    for user in users:
        for link in user.links:
            if link_count.get(link) is None:
                link_count[link] = 1
            else:
                link_count[link] += 1

    popular_link = ""
    popular_link_count = 0
    for link in link_count.keys():
        if link_count[link] > popular_link_count:
            popular_link = link
            popular_link_count = link_count[link]

    return f"most popular - {popular_link}."


def main():
    array_users = []
    try:
        file = open("db.txt", "r", encoding="utf-8")

        for line in file.readlines():
            args = line.split(" | ")
            array_users.append(User(args[0], args[1].replace("\n", "").split(", ")))
        file.close()

        print(getPopularLink(array_users))
    except FileNotFoundError:
        print("Один из файлов не найден")


if __name__ == "__main__":
    main()
