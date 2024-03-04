import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Persiapkan Semua Data
day = pd.read_csv("day.csv")
day.head()
drop_col = ['windspeed']
sns.set(style='white')

for i in day.columns:
  if i in drop_col:
    day.drop(labels=i, axis=1, inplace=True)

# Mengubah Penamaan
day.rename(columns={
    'dteday': 'daydate',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weathercondition',
    'cnt': 'count'
}, inplace=True)

# Mengubah Keterangan
day['weathercondition'] = day['weathercondition'].map({
    1: 'Clear',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Tunderstorm/Fog Snow'
})
day['season'] = day['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day ['month'] = day['month'].map({
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
})
day['weekday'] = day['weekday'].map({
    0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'
})
day['holiday'] = day ['holiday'].map({
    0:'Not_Holiday', 1:'Holiday'
})
day['workingday'] = day['workingday'].map({
    0:'Not_Working', 1:'Working'
})
day['year'] = day['year'].map ({
    0:'2011', 1:'2012'
})

# 2. Mengubah tipe data menjadi 'datetime'
day['daydate'] = pd.to_datetime(day.daydate)

# Menyiapkan daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='daydate').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df

# Menyiapkan daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='daydate').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Menyiapkan daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='daydate').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Menyiapkan monthly_rent_df
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='month').agg({
        'count': 'sum'
    })
    ordered_months = [
        'January','February','March','April','May','June','July',
        'August','September','October','November','December'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_months, fill_value=0)
    return monthly_rent_df

# Menyiapkan weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Menyiapkan workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Menyiapkan holiday_rent_df
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count': 'sum'
    }).reset_index()
    return holiday_rent_df

# Menyiapkan weather_rent_df
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weathercondition').agg({
        'count': 'sum'
    })
    return weather_rent_df

# Membuat komponen filter
min_date = pd.to_datetime(day['daydate']).dt.date.min()
max_date = pd.to_datetime(day['daydate']).dt.date.max()
 
## STREAMLIT EXPLORATION

#slidebar
with st.sidebar:
    # Company Name
    st.image('https://github.com/sxiera/Data-Analysis-Using-Python/blob/main/kisspng-university-of-porto-instituto-superior-de-agronomi-optimize-5b08fbc87ac685.7984766115273154005029.png?raw=true')
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Calendar',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day[(day['daydate'] >= str(start_date)) & 
                (day['daydate'] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

# Membuat judul
st.header('Bike Sharing Analysis Dashboard 📊🚲')

## 1
st.caption ("""Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return 
back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return 
back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of 
over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, 
environmental and health issues. 

Apart from interesting real world applications of bike sharing systems, the characteristics of data being generated by
these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration
of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into
a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important
events in the city could be detected via monitoring these data.""")

st.caption ("created and visualize by Bima Aristo")
st.subheader('1. Tren dalam Peminjaman Sepeda')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df.index,
    monthly_rent_df['count'],
    marker='o', 
    linewidth=2,
    color='#836FFF'
)

for index, row in enumerate(monthly_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)
st.caption ("""Tren peminjaman sepeda menunjukkan peningkatan yang signifikan dari tahun 2011 ke 2012, baik secara keseluruhan maupun pada setiap bulannya. Jumlah peminjaman pada tahun 2012 secara konsisten lebih tinggi daripada tahun sebelumnya. Namun, perlu dicatat bahwa terdapat anomali pada tanggal 29 Oktober 2012 dimana tidak ada peminjaman sepeda, yang dapat dikaitkan dengan kejadian badai Hurricane Sandy.""")
## 2
st.subheader('2. Jumlah Rental Sepeda Ditinjau Dari tipe Casual, Register, dan Keseluruhan')

col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)
 
with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total User', value= daily_rent_total)
    
## 3
st.subheader('3. Jumlah Rental Sepeda Ditinjau dari Musim')

fig, ax = plt.subplots(figsize=(16, 8))
warna_register = "#836FFF"
warna_casual = "#211951"

sns.barplot(
    x='season',
    y='registered',
    data=season_rent_df,
    label='Registered',
    color=warna_register,
    ax=ax
)

sns.barplot(
    x='season',
    y='casual',
    data=season_rent_df,
    label='Casual',
    color=warna_casual,
    ax=ax
)
for index, row in season_rent_df.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)
st.caption ("""Pola peminjaman sepeda bervariasi berdasarkan musimnya, dengan jumlah peminjaman terendah terjadi pada musim panas dan tertinggi pada musim gugur. Hal ini menunjukkan bahwa faktor-faktor selain musim juga memengaruhi jumlah peminjaman, karena bahkan selama musim dingin masih terdapat jumlah peminjaman yang signifikan.
""")

## 4
st.subheader('4. Jumlah Rental Sepeda Ditinjau Dari Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(16, 8))
warna = ["#F0F3FF", "#836FFF", "#211951"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['count'],
    palette=warna,
    ax=ax
)

for index, row in enumerate(weather_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)
st.caption ("""Ada korelasi yang kuat antara kondisi cuaca dan jumlah peminjaman sepeda. Penyewa sepeda cenderung memilih untuk melakukan peminjaman saat cuaca cerah, diikuti oleh kondisi berawan atau berkabut. Sebaliknya, peminjaman sepeda cenderung rendah saat terjadi hujan ringan atau salju ringan.
""")

## 4
st.subheader('5. Jumlah Rental Sepeda Ditinjau Dari Kondisi Temperatur')
fig, ax = plt.subplots(figsize=(14, 6))
warna = "#211951"

sns.scatterplot(
    x='temp',
    y='count',
    data=main_df, 
    alpha=0.7,
    color=warna
)

ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.xlabel('Temperature', fontsize=14)
plt.ylabel('Count', fontsize=14)
st.pyplot(fig)
st.caption("""Terdapat korelasi positif antara suhu dan jumlah peminjaman sepeda, yang terlihat dari pola persebaran data yang cenderung naik ke arah kanan atas pada grafik. Artinya, ketika suhu meningkat, jumlah peminjaman sepeda juga cenderung meningkat. Ini menunjukkan bahwa suhu memainkan peran penting dalam menentukan tingkat minat masyarakat untuk melakukan peminjaman sepeda.""")
