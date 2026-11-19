
import streamlit as st
import mysql.connector
import pandas as pd

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

        db = mysql.connector.connect(
            host="127.0.0.1",
            port=8889,
            user="root",
            password="root",
            database="db_kafe"
        )

        query = "SELECT * FROM menu"
        data = pd.read_sql(query, db)

        st.dataframe(data)

        st.write("Jumlah Menu:", len(data))

        db.close()

    elif pilihan == "Logout":

        st.session_state["login"] = False
        st.session_state["username"] = ""

        st.rerun()
