import numpy as np
import matplotlib.pyplot as plt


def append_file(arg):
    file = open("result.txt", "a", encoding="utf-8")
    file.write(str(arg))
    file.close()


class WeatherData:
    def __init__(self, file_path, color='r'):
        self.__file_path = file_path
        self.__lines = [""]
        self.__arr = []
        self.color = color

    def __update_lines_from_file(self):
        try:
            file = open(self.__file_path)
            self.__lines = file.readlines()
            file.close()
        except FileNotFoundError:
            print(f"FileNotFoundError - {self.__file_path}")

    def __get_statistic(self, line):
        stat_array = line.split()
        return [stat_array[1], stat_array[2], stat_array[3], stat_array[5], stat_array[9], stat_array[7], stat_array[8],
                stat_array[11]]
        # 0 - year, 1 - month, 2 - day, 3 - min temp, 4 - max temp, 5 - mean temp, 6 - status mean temp, 7 - осадки

    def __generate_array(self):
        self.__arr = np.array([self.__get_statistic(line) for line in self.__lines], dtype='f')

    def __get_mean_temperature(self, year, array_month):
        temp = 0.
        count_temp = 0
        for info in self.__arr:
            if year != int(info[0]):
                continue
            if int(info[1]) in array_month:
                if int(info[6]) == 9:
                    continue
                temp += float(info[5])
                count_temp += 1

        try:
            return temp / count_temp
        except ZeroDivisionError:
            return self.__get_mean_temperature(year - 1, array_month)

    def get_temp_years_month_for_graph(self, month):
        def get_years():
            ar = []
            for year in self.__arr:
                year = int(year[0])
                if year not in ar:
                    ar.append(year)
            return ar

        years = get_years()
        return years, [self.__get_mean_temperature(year, month) for year in years]

    def get_center(self, year=2003, month=None):
        if month is None:
            month = []
        temp = []

        for i in self.__arr:
            if int(i[0]) == year and int(i[1]) in month:
                temp.append(i[7])

        np_temp = np.array(temp)
        center = np.sum(np_temp) / np.size(np_temp)

        return center

    def get_dispersion(self, year=2003, month=None):
        if month is None:
            month = []
        temp = []

        for i in self.__arr:
            if int(i[0]) == year and int(i[1]) in month:
                temp.append(i[7])

        np_temp = np.array(temp)
        center = np.sum(np_temp) / np.size(np_temp)

        deviation = np_temp - np.array([center for _ in range(np.size(np_temp))])

        dispersion = np.sum(deviation ** 2) / np.size(np_temp)

        return dispersion

    def __histogram(self, year):
        month = [i for i in range(1, 12)]
        temp = []
        for k in month:
            temp.append(self.get_center(year, [k]))

        plt.subplots()
        plt.bar(month, temp)
        plt.suptitle(f"{self.__file_path} __histogram")

    def __histogram_dispersion(self, year):
        month = [i for i in range(1, 12)]
        temp = []
        for k in month:
            temp.append(self.get_dispersion(year, [k]))

        plt.subplots()
        plt.bar(month, temp)
        plt.suptitle(f"{self.__file_path} __histogram_dispersion")

    def exec(self, year):
        self.__update_lines_from_file()
        self.__generate_array()

        append_file(f"Средняя температура в {year} году за лето в {self.__file_path} = "
                    f"{self.__get_mean_temperature(year, [6, 5, 4])}\n")
        append_file(f"Средняя температура в {year} году за зиму в {self.__file_path} = "
                    f"{self.__get_mean_temperature(year, [12, 1, 2])}\n")

        append_file(f"dispersion = {self.get_dispersion(2003, [i for i in range(1, 13)])}")

        self.__histogram_dispersion(2003)
        self.__histogram(2003)