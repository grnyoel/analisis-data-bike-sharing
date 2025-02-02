import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Proyek Analisis Data: Bike Sharing")

# Load data
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# --- Bagian visualisasi & analisis ---

# Pengaruh musim terhadap pengguna
st.header("Pengaruh Musim terhadap Pengguna")
# ... (Kode visualisasi dengan matplotlib/seaborn) ...
byseason_df = df_day.groupby(by="season").instant.nunique().reset_index()
byseason_df.rename(columns={
    "instant": "sum"
}, inplace=True)

plt.figure(figsize=(10, 5))

sns.barplot(
    y="sum",
    x="season",
    data=byseason_df.sort_values(by="season", ascending=False),
)
plt.title("Number of Bike Sharing by Season", loc="center", fontsize=12)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=10)

# Penggunaan setiap tahun
st.header("Penggunaan Setiap Tahun")

byyr_df = df_day.groupby(by="yr").instant.nunique().reset_index()
byyr_df.rename(columns={
    "instant": "sum"
}, inplace=True)

plt.figure(figsize=(8, 4))

sns.barplot(
    y="sum",
    x="yr",
    data=byyr_df.sort_values(by="yr", ascending=False),
)
plt.title("Number of Bike Sharing by Year", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
st.pyplot(plt)

# Penggunaan setiap bulan
st.header("Penggunaan Setiap Bulan")

plt.figure(figsize=(8, 4))

sns.barplot(
    y="cnt",
    x="mnth",
    data=df_day.sort_values(by="mnth", ascending=False),
)
plt.title("Number of Bike Sharing by Month", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
st.pyplot(plt)

# Penggunaan setiap jam
st.header("Penggunaan Setiap Jam")

plt.figure(figsize=(8, 4))

sns.barplot(
    y="cnt",
    x="hr",
    data=df_hour.sort_values(by="hr", ascending=False),
)
plt.title("Number of Bike Sharing by Hour", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
st.pyplot(plt)

# Kesimpulan

st.header("Kesimpulan")
st.write("1. Berdasarkan visualisasi data, terlihat bahwa musim **Fall** memiliki jumlah pengguna bike sharing terbanyak, diikuti oleh **Summer**, **Winter**, dan **Spring**. Hal ini menunjukkan bahwa musim Fall adalah musim yang paling diminati oleh pengguna bike sharing, sedangkan `Spring` adalah musim yang paling sepi.")
st.write("""2. Berdasarkan visualisasi data, berikut adalah penggunaan dalam setiap tahun, bulan, dan jam:

*   Tahun: Terjadi peningkatan jumlah pengguna bike sharing dari tahun 2011 ke tahun 2012. Hal ini menunjukkan bahwa layanan bike sharing semakin populer dari waktu ke waktu.
*   Bulan: Jumlah pengguna bike sharing cenderung meningkat pada bulan-bulan musim panas seperti Juni, Juli, dan Agustus, dan menurun pada bulan-bulan musim dingin seperti Desember, Januari, dan Februari.
*   Jam: Jumlah pengguna bike sharing cenderung tinggi pada jam-jam sibuk, seperti jam berangkat dan pulang kerja (jam 7-9 pagi dan 5-7 sore).""")