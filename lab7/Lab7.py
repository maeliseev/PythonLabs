from WeatherData import WeatherData
from WeatherBrain import WeatherBrain

"""
Вар 8. 
Таганрог
Краснодар

Функции для работы с атрибутами
"""


def main():
    open("result.txt", "w").close()

    taganrog_data = WeatherData("Taganrog.txt", 'r-')
    taganrog_data.exec(1905)

    krasnodar_data = WeatherData("Krasnodar.txt", 'b--')
    krasnodar_data.exec(1940)

    brain = WeatherBrain()
    brain.get_temp_plot("Таганрог и Краснодар за лето", [taganrog_data, krasnodar_data], [6, 5, 4])
    brain.get_temp_plot("Таганрог и Краснодар за зиму", [taganrog_data, krasnodar_data], [12, 1, 2])

    brain.get_difference_temp(krasnodar_data, taganrog_data)

    brain.show_all_graph()


if __name__ == "__main__":
    main()
