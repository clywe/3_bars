from pprint import pprint
import json


def load_data(filepath):
    with open(filepath) as json_file:
        bars = json.load(json_file)
    return bars.encode("utf-8")


def get_biggest_bar(bars):
    max_bar = bars[0]["Cells"]["SeatsCount"]
    name_bar = bars[0]["Cells"]["Name"]
    for bar in bars:
        if bar["Cells"]["SeatsCount"] > max_bar:
            max_bar = bar["Cells"]["SeatsCount"]
            name_bar = bar["Cells"]["Name"]
    return name_bar


def get_smallest_bar(bars):
    min_bar = bars[0]["Cells"]["SeatsCount"]
    name_bar = bars[0]["Cells"]["Name"]
    for bar in bars:
        if bar["Cells"]["SeatsCount"] < min_bar:
            min_bar = bar["Cells"]["SeatsCount"]
            name_bar = bar["Cells"]["Name"]
    return name_bar


def get_closest_bar(bars, longitude, latitude):
    closest_coordinates = bars[0]["Cells"]["geoData"]["coordinates"]
    dest = abs(longitude - closest_coordinates[0]) +\
        abs(latitude - closest_coordinates[1])
    name_bar = bars[0]["Cells"]["Name"]
    for bar in bars:
        temp_dest =\
            abs(bar["Cells"]["geoData"]["coordinates"][0] - longitude) +\
            abs(bar["Cells"]["geoData"]["coordinates"][1] - latitude)
        if temp_dest < dest:
            dest = temp_dest
            name_bar = bar["Cells"]["Name"]
    return name_bar


if __name__ == '__main__':
    print("Самый большой бар: " + get_biggest_bar(load_data("bars.json")))
    print("Самый маленький бар: " + get_smallest_bar(load_data("bars.json")))
    print("Ближайший бар:" + get_closest_bar(load_data("bars.json"),
                                             37.540921653272,
                                             55.759090897056))
