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
    st.markdown('''
        Dari visualisasi distribusi network_packet_size yang ditampilkan, 
        terlihat pola sebaran ukuran paket jaringan pada seluruh sesi. Histogram menunjukkan frekuensi kemunculan setiap rentang 
        ukuran paket, sementara garis KDE memberikan gambaran trend kepadatan data secara lebih halus.
    ''')

    # Distribusi IP Reputation Score
    st.write('## Distribusi IP Reputation Score')
    fig = plt.figure(figsize=(10,4))
    sns.histplot(data['ip_reputation_score'], kde=True, bins=10)
    plt.title('Histogram of IP Reputation Score')
    st.pyplot(fig)
    st.markdown('''Visualisasi histogram ip_reputation_score menunjukkan sebaran skor reputasi IP dari seluruh sesi yang dianalisis. 
                Garis KDE memberikan gambaran kepadatan distribusi secara lebih halus.
    ''')

    # Jumlah session berdasarkan protocol type
    st.write('## Protocol Type Count')
    fig = plt.figure(figsize=(6,4))
    sns.countplot(x='protocol_type', data=data)
    plt.title('Protocol Type Distribution')
    st.pyplot(fig)
    st.markdown('''Visualisasi countplot ini menampilkan jumlah sesi berdasarkan jenis protokol (protocol_type) yang digunakan dalam dataset.
    ''')

    # Plotly scatter: IP Reputation vs Failed Logins
    st.write('## IP Reputation vs Failed Logins')
    fig_px = px.scatter(data, x='ip_reputation_score', y='failed_logins', color='protocol_type',
                        hover_data=['session_id', 'browser_type'])
    st.plotly_chart(fig_px)
    st.markdown('''Visualisasi scatter plot ini menunjukkan hubungan antara skor reputasi IP (ip_reputation_score) dengan jumlah 
                login gagal (failed_logins), diwarnai berdasarkan protocol_type.
    ''')

    # Heatmap korelasi numerik
    st.write('## Korelasi Fitur Numerik')
    fig = plt.figure(figsize=(8,5))
    sns.heatmap(data[['network_packet_size','login_attempts','session_duration',
                      'ip_reputation_score','failed_logins']].corr(),
                annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    st.pyplot(fig)
    
'''
Berdasarkan hasil analisis korelasi antar fitur, diperoleh temuan sebagai berikut:

1. Tingkat Korelasi Rendah Secara Umum

    Semua nilai korelasi antar fitur berada sangat dekat dengan nol, berkisar antara -0.0135 hingga 0.0216. Hal ini menunjukkan bahwa secara linear, tidak ada hubungan kuat antar fitur pada dataset ini.

2. Pasangan Fitur dengan Korelasi Positif Tertinggi

    * session_duration dengan network_packet_size memiliki korelasi 0.02165 — meskipun tertinggi di tabel, nilainya tetap sangat kecil sehingga hubungannya hampir tidak signifikan.

    * failed_logins dengan ip_reputation_score memiliki korelasi 0.01561, yang juga termasuk lemah.

3. Pasangan Fitur dengan Korelasi Negatif

    * network_packet_size dengan failed_logins memiliki korelasi -0.01167, menunjukkan hubungan negatif yang sangat lemah.

    * login_attempts dengan failed_logins memiliki korelasi -0.01350, yang berarti sedikit indikasi bahwa semakin banyak upaya login, jumlah gagal login justru sedikit menurun, tetapi nilainya terlalu kecil untuk diambil kesimpulan kuat.

4. Implikasi terhadap Modeling

    * Korelasi yang rendah antar fitur ini mengindikasikan bahwa tidak ada masalah multikolinearitas signifikan di dataset.

    * Fitur-fitur yang ada kemungkinan memberikan informasi yang relatif unik, sehingga semuanya masih layak dipertimbangkan dalam proses pemodelan tanpa risiko redundansi yang tinggi.
'''


if __name__ == '__main__':
    run()
