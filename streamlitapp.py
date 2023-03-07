import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import plotly.express as px
import random

random.seed(42)

import os
import sqlite3
import pandas as pd
from datetime import time, datetime, timedelta

st.header('Heart rate')

dbs_dir = r"C:\Users\fnman\HealthData\DBs"
# Connect to the garmin_monitoring.db database
conn = sqlite3.connect(os.path.join(dbs_dir,'garmin_monitoring.db'))

# Calculate the date 90 days ago
_days_ago = datetime.now() - timedelta(days=30)

# Format the date as a string in the expected format for the timestamp attribute
timestamp_filter = _days_ago.strftime("%Y-%m-%d %H:%M:%S")

# Load the monitoring_hr table into a pandas DataFrame, filtered by the last 90 days
query = f"SELECT * FROM monitoring_hr WHERE timestamp >= '{timestamp_filter}'"
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Create a line chart using Plotly Express
fig = px.line(df, x='timestamp', y='heart_rate', title='Heart Rate over Time')

# Plot
st.plotly_chart(fig, use_container_width=True)

#######################
###     SLIDER      ###
#######################


st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

#######################
###     CHART       ###
#######################
st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

############################
###     Select box       ###
############################

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)


############################
###     MULTISELECT      ###
############################
st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
# print(options)
st.write('You selected:', options)

############################
###     checkbox         ###
############################
st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")


# ############################
# ### streamlit components ###
# ############################

# #pip install streamlit-aggrid
# from st_aggrid import AgGrid
# import streamlit as st
# import pandas as pd
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report

# st.header('`streamlit_pandas_profiling`')

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# pr = df.profile_report()
# st_profile_report(pr)

