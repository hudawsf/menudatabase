
import streamlit as st
import pandas as pd
from database import koneksi

def tampilkan_menu():

    st.sidebar.title("☕ Aplikasi Kafe")

    pilihan = st.sidebar.selectbox(
        "Pilih Menu",
        ["Beranda", "Daftar Menu", "Logout"]
    )

    if pilihan == "Beranda":

        st.title("Halaman Beranda")
        st.success("Selamat Datang, " + st.session_state["username"])

    elif pilihan == "Daftar Menu":

        st.title("Daftar Menu Kafe")

        try:
            db = koneksi()

            query = "SELECT * FROM menu"
            data = pd.read_sql(query, db)

            st.dataframe(data)

            st.write("Jumlah Menu:", len(data))

            db.close()

        except Exception as e:
            st.error("Gagal mengambil data menu:")
            st.error(str(e))

    elif pilihan == "Logout":

        st.session_state["login"] = False
        st.session_state["username"] = ""

        st.rerun()
