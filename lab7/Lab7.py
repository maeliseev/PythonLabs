import matplotlib.pyplot as plt
import numpy as np

"""
Вар 8. 
Таганрог
Краснодар

Функции для работы с атрибутами

ЭТО НЕ РАБОТАЕТ ДО КОНЦА
"""


class DataBrain:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__lines = [""]
        self.__arr = []

    def __update_lines_from_file(self):
        try:
            file = open(self.__file_path)
            self.__lines = file.readlines()
            file.close()
        except FileNotFoundError:
            print(f"FileNotFoundError - {self.__file_path}")

    def __get_statistic(self, line):
        stat_array = line.split()
        return [stat_array[1], stat_array[2], stat_array[3], stat_array[5], stat_array[9], stat_array[7], stat_array[8], stat_array[11]]
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

    def __draw_temp_years_month(self, name, month):
        def get_years():
            ar = []
            for year in self.__arr:
                year = int(year[0])
                if year not in ar:
                    ar.append(year)
            return ar

        years = get_years()

        plt.figure(name)
        plt.plot(years, [self.__get_mean_temperature(year, month) for year in years], '--')
        plt.show()

    def exec(self, year):
        self.__update_lines_from_file()
        self.__generate_array()

        print(self.__get_mean_temperature(year, [0, 1, 2]))
        print(self.__get_mean_temperature(year, [4, 5, 6]))
        self.__draw_temp_years_month(f'{self.__file_path}in 4,5,6 month', [4, 5, 6])
        self.__draw_temp_years_month(f'{self.__file_path}in 9,10,11 month', [9, 10, 11])


data = DataBrain("Taganrog.txt")
data.exec(1905)

data2 = DataBrain("Krasnodar.txt")
data2.exec(1940)


