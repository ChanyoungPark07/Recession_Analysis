import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# To-do
# Build a class for parsing all data (FRED API) and visualize
# Write documentation for all class and methods

class Parser:
    def __init__(self, series_id, observation_start, observation_end, key, unit=None):
        """
        Parser Class Constructor
        """

        self.series_id = series_id
        self.observation_start = observation_start
        self.observation_end = observation_end
        self.unit = unit

        try:
            file_path = './api_access/key.txt'
            with open(file_path, 'r') as f:
                self.key = f.read()
        except:
            print('Not a valid key')

    def get_series_observations(self):
        """
        Gets FRED API url based on passed in parameters
        """

        try:
            if (unit == None):
                api_url = f'https://api.stlouisfed.org/fred/series/observations? \
                    series_id={self.series_id} \
                    &observation_start={self.observation_start} \
                    &observation_end={self.observation_end} \
                    &api_key={self.key}&file_type=json'
            else:
                api_url = f'https://api.stlouisfed.org/fred/series/observations? \
                    series_id={self.series_id} \
                    &observation_start={self.observation_start} \
                    &observation_end={self.observation_end} \
                    &units={self.unit}&api_key={self.key}&file_type=json'
        except:
            print('Failed to retrieve data api_url')

        return api_url

    def get_series_data(self):
        """
        Gets data based on api_url
        """

        api_url = get_series_observations(self.series_id, self.observation_start, 
            self.observation_end, self.key, self.unit)

        try:
            response = requests.get(api_url)
            data = response.json()
        except:
            print(f'Failed to retrieve data: {response.status_code}')
        
        return data
