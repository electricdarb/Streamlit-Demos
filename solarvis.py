import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt

# Read in data
solardata = pd.read_csv('Plant_1_Generation_Data.csv')

# Add intro 
st.title('Solar Power Production')

st.markdown(""" ## A data vis demo by Bradford Gill
Dataset: [Solar Power Generation](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data)

Data was collected at an indian solar plant over 34 days. It contains 7 Data points collected from 22 unique
inverters at 15 minute intervals.

 0   DATE_TIME,      object : Date and time of collection \n
 1   PLANT_ID,       int64  : Plant ID that the data was collected at \n
 2   SOURCE_KEY,     object : The ID of inverter \n
 3   DC_POWER,       float64: The DC power collected in the 15 minute interval \n
 4   AC_POWER,       float64: The AC power collected in the 15 minute interval \n
 5   DAILY_YIELD,    float64: The Cumulative sum of power collected from the begining of the day \n
 6   TOTAL_YIELD,    float64: The Cumulative sum of power collected from the begining of the data measurement \n
You can view the code on my [Github](LINKHERE)
""")

st.markdown("""
### Histograms
""")

# define classes 
classes = ['DATE_TIME', 'PLANT_ID', 'SOURCE_KEY', 'DC_POWER', 'AC_POWER', 'DAILY_YIELD', 'TOTAL_YIELD']

# visualize histograms 
fig, ax = plt.subplots()
solardata[['DC_POWER', 'AC_POWER', 'DAILY_YIELD', 'TOTAL_YIELD']].hist(ax = ax)

st.write(fig)

# get unique SOURCE_KEY values 
inverters = solardata['SOURCE_KEY'].unique()

# view AC Power over time
st.markdown("""
### Total Yield Vs Time
casey was here

jk
""")

fig, ax = plt.subplots()
inverters['TOTAL_YIELD'].plot(ax = ax)

st.write(fig)