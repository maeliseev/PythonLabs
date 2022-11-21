"""
Вар 7.
Дано: Множество пользователей и наборы сайтов, которые каждый из них посещает часто
Нужно: Список сайтов, которые посещаются наибольшим или наименьшим числом пользователей
"""


class User:
    def __init__(self, user_name, links):
        self.user_name = user_name
        self.links = links


class UserBrain:
    def __init__(self):
        self.__users = []
        try:
            file = open("db.txt", "r", encoding="utf-8")

            lines = file.readlines()

            for line in lines:
                args = line.split(" | ")
                self.__users.append(User(args[0], args[1].replace("\n", "").split(", ")))

            file.close()
        except FileNotFoundError:
            print("Файл c данными не найден.")

    def get_popular_link(self):
        link_count = {}
        for user in self.__users:
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


def write_in_file(arg):
    file = open("result.txt", "w", encoding="utf-8")
    file.write(arg)
    file.close()


def main():
    brain = UserBrain()
    print(brain.get_popular_link())
    write_in_file(brain.get_popular_link())


if __name__ == "__main__":
    main()
