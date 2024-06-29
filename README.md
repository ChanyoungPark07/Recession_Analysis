# FRED API Recession Analysis

This project provides a comprehensive dashboard for analyzing economic data related to recessions using the FRED API. The dashboard, built with Streamlit, allows users to explore various economic factors over different timeframes and recession periods. The visualization is paired with specific recession context and detailed explanations of the factors behind each recession.

## Streamlit Usage
Get FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html<br /> 
Install all libraries at the top of each file<br /> 
Run `streamlit run` in the terminal to access the Streamlit dashboard<br /> 

## Files

### main.py
This file provides the Streamlit dashboard for the user. It allows users to select economic factors and timeframes, visualize data, and explore historical recessions.

Key Components:<br /> 
Date Range Slider: Enables users to select a date range.<br /> 
Factor Dropdown: Users can select different economic indicators to visualize.<br /> 
Series ID Input: Allows manual input of FRED Series IDs.<br /> 
Visualization: Displays line and scatter plots of the selected economic indicator over time.<br /> 

### parse.py
This file contains the Parser class, which handles data extraction and cleaning from the FRED API.

Key Functions:<br /> 
__init__: Initializes the parser with series ID, start date, end date, and optionally units.<br /> 
get_series_observations: Constructs the API URL based on input parameters.<br /> 
get_series_data: Retrieves data from the FRED API.<br /> 
get_date_value: Extracts date and value pairs from the retrieved data.<br /> 
convert_dataframe: Converts the data into a Pandas DataFrame.<br /> 
visualizer: Creates visualizations for general timeframes.<br /> 
recession_visualizer: Creates visualizations focused on specific recessions.<br /> 

### info.py
This file contains the recession_info dictionary, which provides detailed explanations of the factors behind each major recession.
