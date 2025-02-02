import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul
st.title("Proyek Analisis Data: Bike Sharing")

# Load data
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Mengubah kolom 'dteday' menjadi tipe data datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

# --- Sidebar untuk filter tanggal ---
st.sidebar.header("Rentang Waktu")
start_date = st.sidebar.date_input("Tanggal Awal", df_day["dteday"].min())
end_date = st.sidebar.date_input("Tanggal Akhir", df_day["dteday"].max())

# Filter data berdasarkan tanggal
filtered_df_day = df_day[(df_day["dteday"] >= pd.to_datetime(start_date)) & (df_day["dteday"] <= pd.to_datetime(end_date))]
filtered_df_hour = df_hour[(df_hour["dteday"] >= pd.to_datetime(start_date)) & (df_hour["dteday"] <= pd.to_datetime(end_date))]

# --- Bagian visualisasi & analisis ---

# Pengaruh musim terhadap pengguna
st.header("Pengaruh Musim terhadap Pengguna")
byseason_df = filtered_df_day.groupby(by="season").instant.nunique().reset_index()
byseason_df.rename(columns={"instant": "sum"}, inplace=True)

plt.figure(figsize=(10, 5))
sns.barplot(y="sum", x="season", data=byseason_df.sort_values(by="season", ascending=False))
plt.title("Number of Bike Sharing by Season", loc="center", fontsize=12)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=10)
st.pyplot(plt)

# Penggunaan setiap tahun
st.header("Penggunaan Setiap Tahun")
byyr_df = filtered_df_day.groupby(by="yr").instant.nunique().reset_index()
byyr_df.rename(columns={"instant": "sum"}, inplace=True)

plt.figure(figsize=(8, 4))
sns.barplot(y="sum", x="yr", data=byyr_df.sort_values(by="yr", ascending=False))
plt.title("Number of Bike Sharing by Year", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
st.pyplot(plt)

# Penggunaan setiap bulan
st.header("Penggunaan Setiap Bulan")
plt.figure(figsize=(8, 4))
sns.barplot(y="cnt", x="mnth", data=filtered_df_day.sort_values(by="mnth", ascending=False))
plt.title("Number of Bike Sharing by Month", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
st.pyplot(plt)

# Penggunaan setiap jam
st.header("Penggunaan Setiap Jam")
plt.figure(figsize=(8, 4))
sns.barplot(y="cnt", x="hr", data=filtered_df_hour.sort_values(by="hr", ascending=False))
plt.title("Number of Bike Sharing by Hour", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
st.pyplot(plt)