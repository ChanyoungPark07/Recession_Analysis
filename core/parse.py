import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Parser:
    def __init__(self, series_id, observation_start, observation_end, unit=None):
        """
        Parser Class Constructor
        """

        self.series_id = series_id
        self.observation_start = observation_start
        self.observation_end = observation_end
        self.unit = unit

        try:
            file_path = (
                '/Users/chadpark07/Documents/Data_Science_Projects'
                '/Recession_Analysis/core/api_access/key.txt'
            )
            with open(file_path, 'r') as f:
                self.key = f.read()
        except:
            print('Not a valid key')

    def get_series_observations(self):
        """
        Gets FRED API url based on passed in parameters
        """
        
        try:
            if (self.unit == None):
                api_url = (
                    f'https://api.stlouisfed.org/fred/series/observations?'
                    f'series_id={self.series_id}'
                    f'&observation_start={self.observation_start}'
                    f'&observation_end={self.observation_end}'
                    f'&api_key={self.key}'
                    f'&file_type=json'
                )
            else:
                api_url = (
                    f'https://api.stlouisfed.org/fred/series/observations?'
                    f'series_id={self.series_id}'
                    f'&observation_start={self.observation_start}'
                    f'&observation_end={self.observation_end}'
                    f'&units={self.unit}'
                    f'&api_key={self.key}'
                    f'&file_type=json'
                )
        except:
            print('Failed to retrieve data api_url')

        return api_url

    def get_series_data(self):
        """
        Gets data based on api_url
        """

        api_url = self.get_series_observations()

        try:
            response = requests.get(api_url)
            data = response.json()
        except:
            print(f'Failed to retrieve data: {response.status_code}')
        
        return data
    

p1 = Parser('GDP', '2007-01-01', '2010-01-01')
print(p1.get_series_data())
