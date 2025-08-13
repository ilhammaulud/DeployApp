import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image


def run():
    # Header
    st.write('# Cybersecurity Session Data Analysis')

    # Latar belakang
    st.write('# Latar Belakang')
    st.markdown('''
        Dataset ini berisi informasi sesi login pengguna yang digunakan untuk
        menganalisis potensi serangan siber. Fitur-fitur mencakup ukuran paket,
        jenis protokol, jumlah percobaan login, reputasi IP, dan aktivitas
        yang tidak biasa.
    ''')

    # Dataset
    data = pd.read_csv('dataset.csv')



    # Tampilkan dataset
    st.write('# Dataset')
    st.dataframe(data)

    # EDA
    st.write("# Exploratory Data Analysis")

    # Distribusi Network Packet Size
    st.write('## Distribusi Network Packet Size')
    fig = plt.figure(figsize=(10,4))
    sns.histplot(data['network_packet_size'], kde=True, bins=10)
    plt.title('Histogram of Network Packet Size')
    st.pyplot(fig)

    # Distribusi IP Reputation Score
    st.write('## Distribusi IP Reputation Score')
    fig = plt.figure(figsize=(10,4))
    sns.histplot(data['ip_reputation_score'], kde=True, bins=10)
    plt.title('Histogram of IP Reputation Score')
    st.pyplot(fig)

    # Jumlah session berdasarkan protocol type
    st.write('## Protocol Type Count')
    fig = plt.figure(figsize=(6,4))
    sns.countplot(x='protocol_type', data=data)
    plt.title('Protocol Type Distribution')
    st.pyplot(fig)

    # Plotly scatter: IP Reputation vs Failed Logins
    st.write('## IP Reputation vs Failed Logins')
    fig_px = px.scatter(data, x='ip_reputation_score', y='failed_logins', color='protocol_type',
                        hover_data=['session_id', 'browser_type'])
    st.plotly_chart(fig_px)

    # Heatmap korelasi numerik
    st.write('## Korelasi Fitur Numerik')
    fig = plt.figure(figsize=(8,5))
    sns.heatmap(data[['network_packet_size','login_attempts','session_duration',
                      'ip_reputation_score','failed_logins']].corr(),
                annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    st.pyplot(fig)

if __name__ == '__main__':
    run()
