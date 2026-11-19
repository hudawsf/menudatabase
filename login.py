
import streamlit as st
import mysql.connector
import menu

# Mengecek status login
if "login" not in st.session_state:
    st.session_state["login"] = False


# =====================
# HALAMAN LOGIN
# =====================

if not st.session_state["login"]:

    st.title("☕ Aplikasi Kafe")

    pilihan = st.radio(
        "Pilih Aktivitas",
        ["Login", "Register"],
        horizontal=True
    )

    # LOGIN
    if pilihan == "Login":

        st.subheader("Login Pengguna")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Masuk"):

            db = mysql.connector.connect(
                host="127.0.0.1",
                port=8889,
                user="root",
                password="root",
                database="db_kafe"
            )

            cursor = db.cursor()

            sql = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))

            hasil = cursor.fetchone()

            if hasil:
                st.session_state["login"] = True
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("Login Gagal!")

            cursor.close()
            db.close()

    # REGISTER
    elif pilihan == "Register":

        st.subheader("Pendaftaran Pengguna Baru")

        nama = st.text_input("Nama")
        username = st.text_input("Username Baru")
        password = st.text_input("Password Baru", type="password")

        if st.button("Daftar"):

            db = mysql.connector.connect(
                host="127.0.0.1",
                port=8889,
                user="root",
                password="root",
                database="db_kafe"
            )

            cursor = db.cursor()

            sql = """
            INSERT INTO users (nama, username, password)
            VALUES (%s, %s, %s)
            """

            cursor.execute(sql, (nama, username, password))
            db.commit()

            st.success("Register Berhasil!")

            cursor.close()
            db.close()


# =====================
# HALAMAN MENU
# =====================

else:
    menu.tampilkan_menu()
