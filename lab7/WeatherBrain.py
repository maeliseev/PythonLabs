import matplotlib.pyplot as plt
import numpy as np

from WeatherData import WeatherData


def append_file(arg):
    file = open("result.txt", "a", encoding="utf-8")
    file.write(str(arg))
    file.close()


class WeatherBrain:
    @staticmethod
    def show_all_graph():
        plt.show()

    @staticmethod
    def get_temp_plot(name, weather_data=None, month_list=None):
        if month_list is None:
            month_list = []
        if weather_data is None:
            weather_data = [WeatherData("Taganrog.txt")]

        plt.figure(name)
        for data in weather_data:
            args = data.get_temp_years_month_for_graph(month_list)
            plt.plot(args[0], args[1], data.color)

    @staticmethod
    def get_difference_temp(weather_data1, weather_data2):
        if weather_data1 is None:
            weather_data1 = WeatherData("Taganrog.txt")
        if weather_data2 is None:
            weather_data2 = WeatherData("Taganrog.txt")

        arr1 = np.array(weather_data1.get_temp_years_month_for_graph(range(1, 13))[1], dtype='f')
        arr2 = np.array(weather_data2.get_temp_years_month_for_graph(range(1, 13))[1], dtype='f')

        if arr1.size > arr2.size:
            arr2 = np.insert(arr2, -1, [0. for _ in range(arr1.size - arr2.size)])
        else:
            arr1 = np.insert(arr1, -1, [0. for _ in range(arr2.size - arr1.size)])

        append_file(f"Разность среднегодовой температуры:\n{arr1 - arr2}")
