import streamlit as st
from core.parse import Parser

p1 = Parser('GDP', '2007-01-01', '2010-01-01')
p1_data = p1.get_series_data()
p1_data_cleaned = p1.get_date_value(p1_data)
p1_data_df = p1.convert_dataframe(p1_data_cleaned)
fig = p1.visualizer(p1_data_df)

st.write('Recession Dashboard')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)
