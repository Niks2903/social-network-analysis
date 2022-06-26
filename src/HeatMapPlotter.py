#from geopy.geocoders import Nominatim
import gmaps
import gmplot
import pandas as pd
import gmaps.datasets
import matplotlib.pyplot as plt
import folium

class HeatMapPlotter:

    # def plot_map_locations(self, read_filename, store_filename):
    #     df = pd.read_csv(read_filename)
    #     location_array = []
    #     for i in df.index:
    #         location_array.append(df.at[i, "Location"])
    #     HeatMapPlotter.plot_map(location_array, store_filename)
    #
    # def plot_map_places(self, read_file_name, store_filename):
    #     df = pd.read_csv(read_file_name)
    #     places_array = []
    #     for i in df.index:
    #         places_array.append(df.at[i, "Place"])
    #     HeatMapPlotter.plot_map(places_array, store_filename)

    @staticmethod
    def plot_map(read_filename, store_filename):
        # geolocator = Nominatim()
        #
        # coordinates = {'latitude': [], 'longitude': []}
        # for count, user_loc in enumerate(location_array):
        #     try:
        #         location = geolocator.geocode(user_loc)
        #         if location:
        #             print("Location: True")
        #             coordinates['latitude'].append(location.latitude)
        #             coordinates['longitude'].append(location.longitude)
        #             print(location)
        #     except:
        #         print("Except")
        #         pass
        #
        df = pd.read_csv(read_filename)
        longitude = df["Longitudes"]
        latitude = df["Latitudes"]
        print(longitude)

        # # Instantiate and center a GoogleMapPlotter object to show our map
        # gmap = gmplot.GoogleMapPlotter(30, 0, 3, apikey="AIzaSyAaVke5Ksf3G0Y8anmguKnr8T-xBHmmuI8")
        #
        # # Insert points on the map passing a list of latitudes and longitudes
        # gmap.heatmap(latitude, longitude, radius=10)
        # # Save the map to html file
        # gmap.draw(store_filename)

        m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)

        # I can add marker one by one on the map
        for i in range(0, len(longitude)):
            folium.Marker([latitude[i], longitude[i]]).add_to(m)

        # Save it as html
        m.save(store_filename)

        # gmaps.configure(api_key="AIzaSyAaVke5Ksf3G0Y8anmguKnr8T-xBHmmuI8")  # Your Google API key
        # df = gmaps.datasets.load_dataset_as_df('starbucks_kfc_uk')
        # print(df)
        # # load a Numpy array of (latitude, longitude) pairs
        # #locations = gmaps.datasets.load_dataset("taxi_rides")
        # starbucks_df = df[df['chain_name'] == 'starbucks']
        # starbucks_df = starbucks_df[['latitude', 'longitude']]
        #
        # starbucks_layer = gmaps.symbol_layer(
        #     starbucks_df, fill_color="green", stroke_color="green", scale=2
        # )
        # fig = gmaps.figure()
        # fig.add_layer(starbucks_layer)
        #


if __name__ == "__main__":
    heat_map_plotter = HeatMapPlotter()
    heat_map_plotter.plot_map("CoordinatesLocation.csv","/home/aniketwalse/testDjango/testApp/templates/testApp/location_map_pulwama.html")
    heat_map_plotter.plot_map("CoordinatesPlaces.csv","/home/aniketwalse/testDjango/testApp/templates/testApp/places_map_pulwama.html")
