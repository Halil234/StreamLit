import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title('Hello Wilders, welcome to my Car application!')



link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_allcar = pd.read_csv(link)

region = st.radio(
     "Please choose one Region you want to analyse",
     (' US.', ' Europe.', ' Japan.', 'All.'))

if region == ' US.':
    st.write('You selected US.')
    df_car = df_allcar.loc[(df_allcar["continent"] == region)]
elif region == ' Europe.':
    st.write("You selected Europe.")
    df_car = df_allcar.loc[(df_allcar['continent'] == region)]
elif region == ' Japan.':
    st.write("You selected Japan.")
    df_car = df_allcar.loc[(df_allcar['continent'] == region)]
elif region == 'All.':
    df_car = df_allcar

st.write("Here the pure car data:")

df_car
#df_allcar.loc[df_allcar["continent"] == 'Japan.']

# st.line_chart(df_weather['MAX_TEMPERATURE_C'])




st.write("Here the correlation heatmap:")

viz_correlation = sns.heatmap(df_car.corr(),
    center=0,
    cmap = sns.color_palette("vlag", as_cmap=True)
    )
st.pyplot(viz_correlation.figure)

st.write("Here the distribution of the car dataframe:")

fig, axs = plt.subplots(4,2, figsize=(24, 20))

axe = axs.ravel()

axe[0].set_title('mpg',fontsize=20)
axe[1].set_title('cylinders',fontsize=20)
axe[2].set_title('cubicinches',fontsize=20)
axe[3].set_title('hp',fontsize=20)
axe[4].set_title('weightlbs',fontsize=20)
axe[5].set_title('time to 60',fontsize=20)
axe[6].set_title('year',fontsize=20)
axe[7].set_title('continent',fontsize=20)




df_car['mpg'].hist(ax=axe[0])
df_car['cylinders'].hist(ax=axe[1])
df_car['cubicinches'].hist(ax=axe[2])
df_car['hp'].hist(ax=axe[3])
df_car['weightlbs'].hist(ax=axe[4])
df_car['time-to-60'].hist(ax=axe[5])
df_car['year'].hist(ax=axe[6])
df_car['continent'].hist(ax=axe[7])

#df_car.plot.hist(bins=50, alpha=0.7,  title="Average Measurements per Tumor Type")
plt.show()
st.pyplot(fig)


name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")