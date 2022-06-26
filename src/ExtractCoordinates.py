import pandas as pd
import json
import numpy as np


longitude_location = []
latitude_location = []

longitude_places = []
latitude_places = []


def convert_coordinates_location(coordinates):
    longitude_avg = 0
    latitude_avg = 0
    for coordinate in coordinates:
        longitude_avg += coordinate[0]
        latitude_avg += coordinate[1]
        print(coordinates," : ",longitude_avg," : ",latitude_avg)
    longitude_location.append(longitude_avg/4)
    latitude_location.append(latitude_avg/4)


def convert_coordinates(coordinates):
    longitude_avg = 0
    latitude_avg = 0
    coordinates = coordinates[0]
    for coordinate in coordinates:
        longitude_avg += coordinate[0]
        latitude_avg += coordinate[1]
        print(coordinates," : ",longitude_avg," : ",latitude_avg)

    longitude_places.append(longitude_avg/4)
    latitude_places.append(latitude_avg/4)


if __name__ == "__main__":
    tweets = []
    for line in open("pulwamadata50000.txt", "r"):
        tweets.append(json.loads(line))
    for tweet in tweets:
        if tweet["coordinates"]:
            if tweet["coordinates"]["type"] == "Point":
                longitude_location.append(tweet["coordinates"]["coordinates"][0])
                latitude_location.append(tweet["coordinates"]["coordinates"][1])
            else:
                convert_coordinates_location(tweet["coordinates"]["coordinates"])
    for tweet in tweets:
        if tweet["place"]:
            if tweet["place"]["bounding_box"]["type"] == "Point":
                longitude_places.append(tweet["place"]["bounding_box"]["coordinates"][0][0])
                latitude_places.append(tweet["place"]["bounding_box"]["coordinates"][0][1])
            else:
                convert_coordinates(tweet["place"]["bounding_box"]["coordinates"])
    df = pd.DataFrame(data=[value for value in longitude_location], columns=["Longitudes"])
    df["Latitudes"] = np.array([value for value in latitude_location])
    df.to_csv("CoordinatesLocation.csv", mode="w")

    df = pd.DataFrame(data=[value for value in longitude_places], columns=["Longitudes"])
    df["Latitudes"] = np.array([value for value in latitude_places])
    df.to_csv("CoordinatesPlaces.csv", mode="w")
