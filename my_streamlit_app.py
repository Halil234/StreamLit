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

fig, axs = plt.subplots(1,2)

df_car['mpg'].hist(ax=axs[0])
df_car['cylinders'].hist(ax=axs[1])

#df_car.plot.hist(bins=50, alpha=0.7,  title="Average Measurements per Tumor Type")
plt.show()
st.pyplot(fig)


name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")