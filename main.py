import streamlit as st
from datetime import datetime
from core.parse import Parser
from core.info import recession_info

# Dashboard Title
st.title('FRED API Recession Dashboard')

# Start and End Date for Slider
min_date = datetime(1970, 1, 1)
max_date = datetime.today()

# Session State for Slider
if 'slider' not in st.session_state:
    st.session_state['slider'] = (min_date, max_date)

# Dictionary for Series IDs
series_id_dict = {
    'Gross Domestic Product': 'GDP',
    'Unemployment Rate': 'UNRATE',
    'Personal Consumption Expenditures': 'PCE',
    'Personal Consumption Expenditures Excluding Food and Energy': 'DPCCRV1Q225SBEA',
    'NASDAQ Composite Index': 'NASDAQCOM',
    'All-Transactions House Price Index': 'USSTHPI'
    }

# Dropdown Box for Recession Factors
factor_option = st.selectbox(
    'Choose a Factor to Explore:',
    ('Gross Domestic Product', 
    'Unemployment Rate', 
    'Personal Consumption Expenditures', 
    'Personal Consumption Expenditures Excluding Food and Energy', 
    'NASDAQ Composite Index', 
    'All-Transactions House Price Index')
    )

# Input box for Series ID
factor_input = st.text_input(
    label='Enter a Series ID from the FRED Website - https://fred.stlouisfed.org',
    value=None,
    placeholder='Type Input Here and Press Enter'
    )

# Date Slider
date_slider = st.slider(
    'Select a Date Range:', 
    min_value=min_date, 
    max_value=max_date,
    value=st.session_state['slider'],
    format='YYYY-MM-DD',
    key='slider'
    )

# Get Data Using Recession Factor and Dates and Visualize
if factor_input is not None:
    series_id = factor_input
else:
    series_id = series_id_dict[factor_option]

start_date, end_date = st.session_state['slider']
start_date = st.session_state['slider'][0].strftime('%Y-%m-%d')
end_date = st.session_state['slider'][1].strftime('%Y-%m-%d')

try:
    p1 = Parser(series_id, start_date, end_date)
    p1_data = p1.get_series_data()
except KeyError as e:
    st.write('Invalid Series ID Input - Please Double Check if Input Exists in FRED Website')
    series_id = series_id_dict[factor_option]
    p1 = Parser(series_id, start_date, end_date)
    p1_data = p1.get_series_data()

p1_data_cleaned = p1.get_date_value(p1_data)

if (len(p1_data_cleaned) <= 5):
    st.write('Invalid Timeframe - Choose a Larger Timeframe!')
else:
    p1_data_df = p1.convert_dataframe(p1_data_cleaned)
    fig = p1.visualizer(p1_data_df, start_date, end_date)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig) 

# Dictionary for Recession Names and Dates
recessions_dates = {
    '1973–1975 Recession': ('1973-11-01', '1975-03-01'),
    '1980 Recession': ('1980-01-01', '1980-07-01'),
    '1981-1982 Recession': ('1981-07-01', '1982-11-01'),
    'Early 1990s Recession': ('1990-07-01', '1991-03-01'),
    'Early 2000s Recession': ('2001-03-01', '2001-11-01'), 
    'Great Recession': ('2007-12-01', '2009-06-01'),
    'COVID-19 Recession': ('2020-02-01', '2020-04-01')
    }

# Dropdown Box for Recessions Names in History
recession_option = st.selectbox(
    'Choose a Recession to Explore:',
    ('1973–1975 Recession', 
    '1980 Recession', 
    '1981-1982 Recession', 
    'Early 1990s Recession', 
    'Early 2000s Recession', 
    'Great Recession',
    'COVID-19 Recession')
    )

# Get Data Using Recession Name and Dates and Visualize
start_date, end_date = recessions_dates[recession_option]

try:
    p1 = Parser(series_id, start_date, end_date)
    p1_data = p1.get_series_data()
    p1_data_cleaned = p1.get_date_value(p1_data)
    p1_data_df = p1.convert_dataframe(p1_data_cleaned)
    fig = p1.recession_visualizer(p1_data_df, start_date, end_date, recession_option)
    st.pyplot(fig)
except KeyError as e:
    st.write(
        'Recession Data May Not Be Available for this Series ID - Try a Different Recession'
        )

# Explanation of Factors Behind each Recession
st.markdown(recession_info[recession_option])
