import requests
import numpy as np
import pandas as pd
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
        
        return data['observations']

    def get_date_value(self, data):
        """
        Gets dates and values from the data
        """

        return [{'date':values['date'], 'value':values['value']} for values in data]

    def convert_dataframe(self, data):
        """
        Converts data into dataframe
        """

        data_df = pd.DataFrame(data)
        data_df = data_df.drop(list(data_df[data_df['value'] == '.'].index))
        data_df['value'] = data_df['value'].astype('float')
        return data_df

    def visualizer(self, df):
        """
        Visualizes dataframe using line plot
        """

        sns.relplot(data=df, x='date', y='value', kind='line')

        if (len(df) > 30):
            dates = []
            idx = 0
            for date in list(df['date']):
                if idx % 10 == 0:
                    dates.append(date)
                idx += 1
            plt.xticks(dates)

        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.xticks(rotation=90)
        plt.tight_layout()
