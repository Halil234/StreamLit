import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title('Hello Wilders, welcome to my Car application!')



link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)


st.write("Here the pure car data:")

df_car

# st.line_chart(df_weather['MAX_TEMPERATURE_C'])




st.write("Here the correlation heatmap:")

viz_correlation = sns.heatmap(df_car.corr(),
    center=0,
    cmap = sns.color_palette("vlag", as_cmap=True)
    )
st.pyplot(viz_correlation.figure)

st.write("Here the distribution of the car dataframe:")

fig, ax = plt.subplots()

a_heights, a_bins = np.histogram(df_car['A'])
b_heights, b_bins = np.histogram(df_car['B'], bins=a_bins)

width = (a_bins[1] - a_bins[0])/3

ax.bar(a_bins[:-1], a_heights, width=width, facecolor='cornflowerblue')
ax.bar(b_bins[:-1]+width, b_heights, width=width, facecolor='seagreen')

df_car.hist()

fig, ax = plt.subplots(figsize=(15,3))
#df_car.plot.hist(bins=50, alpha=0.7,  title="Average Measurements per Tumor Type")
plt.show()
st.pyplot(fig)


name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")