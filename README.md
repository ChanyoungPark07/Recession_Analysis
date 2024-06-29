# FRED API Recession Analysis

This project provides a comprehensive dashboard for analyzing economic data related to recessions using the FRED API. The dashboard, built with Streamlit, allows users to explore various economic factors over different timeframes and recession periods. The visualization is paired with specific recession context and detailed explanations of the factors behind each recession.

## Streamlit Usage
Get FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html<br />  
Install all libraries at the top of each file
Run '''streamlit run''' in the terminal to access the Streamlit dashboard

## Files

### main.py
This file provides the Streamlit dashboard for the user. It allows users to select economic factors and timeframes, visualize data, and explore historical recessions.

Key Components:
Date Range Slider: Enables users to select a date range.
Factor Dropdown: Users can select different economic indicators to visualize.
Series ID Input: Allows manual input of FRED Series IDs.
Visualization: Displays line and scatter plots of the selected economic indicator over time.

### parse.py
This file contains the Parser class, which handles data extraction and cleaning from the FRED API.

Key Functions:
__init__: Initializes the parser with series ID, start date, end date, and optionally units.
get_series_observations: Constructs the API URL based on input parameters.
get_series_data: Retrieves data from the FRED API.
get_date_value: Extracts date and value pairs from the retrieved data.
convert_dataframe: Converts the data into a Pandas DataFrame.
visualizer: Creates visualizations for general timeframes.
recession_visualizer: Creates visualizations focused on specific recessions.

### info.py
This file contains the recession_info dictionary, which provides detailed explanations of the factors behind each major recession.
