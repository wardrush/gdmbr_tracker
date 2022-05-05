# Hold helper functions for the main flask app here

### Imports ###
import pandas as pd
import os
import requests
from xml.etree import ElementTree

### Set the Stage ###
def create_location_data_file(debug=False):
# TODO Create function that checks for existing CSV with location data
# if its not there, create a CSV with relevant columns
    print('Checking for existing location data CSV')
    filepath = os.path.join("/home", "wardrush", "mysite", "data", "GDMBR-2022_rawdata.csv")
    # SPOT XML columns
    cols = ['id',
            'messengerId',
            'messengerName',
            'unixTime',
            'messageType',
            'latitude',
            'longitude',
            'modelId',
            'showCustomMsg',
            'dateTime',
            'hidden',
            'messageContent',
            '_clientUnixTime']
    # if file does not exist create
    if not os.path.exists(filepath):
        print(f'File not found. Creating at "{filepath}"')
        df = pd.DataFrame(columns=cols)
        if debug==True:
            print(df.head())
            df.to_csv(filepath)
            print('Success')
        else:
            df.to_csv(filepath)
    else:
        print(f'File "{filepath}" already exists')
        print('Continuing...')

def get_spot_api_key():
    return '0ArVRndOpKVJJGqc5hN7uGHzV34r5vUko'

### Get the Location ####
def get_spot_location_data(debug=False):
    # TODO make the API request to SPOT
    baseurl1 = "https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/"
    baseurl2 = "/message.json"
    r = requests.post(baseurl1+get_spot_api_key()+baseurl2)

    # parse into XML tree directly from string
    df = pd.read_json(baseurl)
    print(df.head)


### Process location data ###
def get_current_lat():
    # TODO pick the most recent lat from the SPOT API call
    # return
    pass

def get_current_long():
    # TODO pick the most recent long from the SPOT API call
    pass

### Build the Map ###
def get_mapbox_accesskey():
    # returns the mapbox access key
    return 'pk.eyJ1Ijoid2FyZHJ1c2giLCJhIjoiY2wyNnR4bmplMDJkaDNqcjAxZm00OW94OCJ9.sDTtXh2pZMctCLrNAQgHaw'

def get_route_data():
    # Create function that returns the lat longs correctly formatted for MapBox
    # MapBox accepts list of lists
    # Reads CSV data stored in GDMBR-2021_v2_10k-point.csv
    filepath = os.path.join("/home", "wardrush", "mysite", "data", "GDMBR-2021_v2_10k-point.csv")
    df = pd.read_csv(filepath)
    route_longs = df['Long'].to_list()
    route_lats = df['Lat'].to_list()
    route_data = [[long, lat] for long, lat in zip(route_longs,route_lats)]

    return route_data
# TODO

if __name__ == "__main__":
    get_spot_location_data(debug=True)
