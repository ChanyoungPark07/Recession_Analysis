import streamlit as st
from datetime import datetime
from core.parse import Parser

# Dashboard Title
st.title('Recession Dashboard')

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
    'Personal Consumption Expenditures (PCE) Excluding Food and Energy': 'DPCCRV1Q225SBEA',
    'NASDAQ Composite Index': 'NASDAQCOM',
    'All-Transactions House Price Index': 'USSTHPI'
    }

# Dropdown Box for Recession Factors
factor_option = st.selectbox(
    'Choose a Factor to Explore:',
    ('Gross Domestic Product', 
    'Unemployment Rate', 
    'Personal Consumption Expenditures', 
    'Personal Consumption Expenditures (PCE) Excluding Food and Energy', 
    'NASDAQ Composite Index', 
    'All-Transactions House Price Index')
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
series_id = series_id_dict[factor_option]
start_date, end_date = st.session_state['slider']
start_date = st.session_state['slider'][0].strftime('%Y-%m-%d')
end_date = st.session_state['slider'][1].strftime('%Y-%m-%d')

p1 = Parser(series_id, start_date, end_date)
p1_data = p1.get_series_data()
p1_data_cleaned = p1.get_date_value(p1_data)

if (len(p1_data_cleaned) <= 5):
    st.write("**Important**: Choose a Larger Timeframe!")
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

p1 = Parser(series_id, start_date, end_date)
p1_data = p1.get_series_data()
p1_data_cleaned = p1.get_date_value(p1_data)
p1_data_df = p1.convert_dataframe(p1_data_cleaned)
fig = p1.recession_visualizer(p1_data_df, start_date, end_date, recession_option)
st.pyplot(fig)

# Explanation of Factors Behind each Recession
if (recession_option == '1973–1975 Recession'):
    st.markdown(
        """
        Information about the 1973–1975 Recession:
        
        """
    )
elif (recession_option == '1980 Recession'):
    st.markdown(
        """
        Information about the 1980 Recession:
        
        """
    )
elif (recession_option == '1981-1982 Recession'):
    st.markdown(
        """
        Information about the 1981-1982 Recession:
        
        """
    )
elif (recession_option == 'Early 1990s Recession'):
    st.markdown(
        """
        Information about the Early 1990s Recession:
        
        """
    )
elif (recession_option == 'Early 2000s Recession'):
    st.markdown(
        """
       Information about the Early 2000s Recession:
        
        """
    )
elif (recession_option == 'Great Recession'):
    st.markdown(
        """
        Information about the Great Recession:
        
        """
    )
elif (recession_option == 'COVID-19 Recession'):
    st.markdown(
        """
        Information about the COVID-19 Recession:
        
        """
    )