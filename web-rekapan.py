import streamlit as st
import pandas as pd

st.title("Rekapan Pengunjung RSIA HIMAH SAWI")
# tanggal = st.date_input("When's your birthday")
# st.text(tanggal)
st.markdown('---')
st.markdown("Pilih File Yang ingin Anda Import")
uploaded_file = st.file_uploader(
    " ", type="csv")

if uploaded_file:
    st.markdown('---')
    df = pd.read_csv(uploaded_file)
    df["Nomer Telepon"] = df["Nomer Telepon"].apply(lambda x: str(x))
    df["Masukkan Nomer Rekam Medis Jika Peserta Lama"] = df["Masukkan Nomer Rekam Medis Jika Peserta Lama"].apply(lambda x: str(x))
    df['Masukkan Nomer Rekam Medis Jika Peserta Lama'] = df['Masukkan Nomer Rekam Medis Jika Peserta Lama'].astype(str).str.replace('.0', '')
    df = st.dataframe(df)
    tanggal = st.text_input(
        "Masukkan Tanggal Yang Ingin dicari (Tahun-Bulan-Tangaal)")
    tombol = st.button("Cari Data")
    if tombol:
        df_new = df[df['Pilih Tanggal Rencana Kunjungan'] == tanggal]
        df_new
        download = st.button("Download")
