import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

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
        data_df['date'] = pd.to_datetime(data_df['date'])
        return data_df

    def visualizer(self, df, start_date, end_date):
        """
        Visualizes dataframe given start and end dates using line and scatterplots
        """

        sns.relplot(data=df, x='date', y='value', kind='line', 
            color='blue', height=5, aspect=2)

        df_length = len(df)

        if (df_length > 10):
            dates = df['date'][::df_length//10]
            plt.xticks(dates)
        else:
            dates = df['date']

        scatter_df = df[df['date'].isin(dates)]
        sns.scatterplot(data=scatter_df, x='date', y='value', color='red')

        plt.title(f'FRED API Plot - {self.series_id}')
        
        recessions_dates = [
            ('1973-11-01', '1975-03-01'),
            ('1980-01-01', '1980-07-01'),
            ('1981-07-01', '1982-11-01'),
            ('1990-07-01', '1991-03-01'),
            ('2001-03-01', '2001-11-01'), 
            ('2007-12-01', '2009-06-01'),
            ('2020-02-01', '2020-04-01')
            ]
        for recession in recessions_dates:
            if (recession[0] > start_date and recession[1] < end_date):
                plt.fill_between([recession[0], recession[1]], 
                    min(df['value']), max(df['value']), color='gray', alpha=0.35)

        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.xticks(rotation=90)
        plt.grid()
        plt.tight_layout()


    def recession_visualizer(self, df, start_date, end_date, name):
        """
        Visualizes a spcific recession using line and scatterplots
        """

        sns.relplot(data=df, x='date', y='value', kind='line', 
            color='blue', height=5, aspect=2)

        df_length = len(df)

        if (df_length > 10):
            dates = df['date'][::df_length//10]
            plt.xticks(dates)
        else:
            dates = df['date']

        scatter_df = df[df['date'].isin(dates)]
        sns.scatterplot(data=scatter_df, x='date', y='value', color='red')

        plt.title(f'FRED API {name} Plot - {self.series_id}')

        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.xticks(rotation=90)
        plt.grid()
        plt.tight_layout()
