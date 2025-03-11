import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Dashboard ini menyajikan analisis data peminjaman sepeda berdasarkan musim, suhu, dan faktor lainnya.")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    return df

df = load_data()

# Menampilkan Data
st.subheader("Tampilkan Data")
st.write(df.head())

# Analisis 1: Pola Peminjaman Sepeda Berdasarkan Musim
st.subheader("Pola Peminjaman Sepeda Berdasarkan Musim")
season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
df['season_label'] = df['season'].map(season_labels)

fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x='season_label', y='cnt', data=df, palette='viridis', ax=ax)
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.title('Distribusi Penyewaan Sepeda Berdasarkan Musim')
st.pyplot(fig)

# Analisis 2: Hubungan antara Suhu dan Jumlah Peminjam
st.subheader("Hubungan antara Suhu dan Jumlah Peminjam")
fig, ax = plt.subplots(figsize=(8,5))
sns.scatterplot(x='temp', y='cnt', data=df, alpha=0.5)
plt.xlabel('Suhu Normalisasi')
plt.ylabel('Jumlah Peminjam Sepeda')
plt.title('Hubungan antara Suhu dan Jumlah Peminjam')
st.pyplot(fig)

# Korelasi
correlation = df[['temp', 'cnt']].corr().iloc[0,1]
st.write(f"Korelasi antara suhu dan jumlah peminjaman: {correlation:.2f}")

# Analisis Tambahan: Rata-rata Penyewaan Sepeda per Hari dalam Seminggu
st.subheader("Rata-rata Penyewaan Sepeda per Hari dalam Seminggu")
day_labels = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
df['weekday_label'] = df['weekday'].map(day_labels)

day_avg = df.groupby('weekday_label')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='weekday_label', y='cnt', data=day_avg, palette='coolwarm', ax=ax)
plt.xlabel('Hari')
plt.ylabel('Rata-rata Penyewaan')
plt.title('Rata-rata Penyewaan Sepeda per Hari dalam Seminggu')
st.pyplot(fig)

# Menampilkan Insight
st.subheader("Insight")
st.write("1. Peminjaman sepeda tertinggi terjadi pada musim Fall, sedangkan Spring memiliki jumlah penyewaan terendah.")
st.write("2. Terdapat korelasi positif antara suhu dan jumlah peminjaman sepeda (r = 0.63), artinya semakin hangat suhu, semakin banyak peminjam.")
st.write("3. Hari kerja cenderung memiliki jumlah peminjam yang lebih tinggi dibandingkan akhir pekan.")
