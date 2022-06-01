import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

df_car.hist()

fig, ax = plt.subplots(3, 3, tight_layout=True)
plt.show()
st.pyplot(fig)


name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")