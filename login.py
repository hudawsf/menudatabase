
import streamlit as st
from database import koneksi
import menu

# Mengecek status login
if "login" not in st.session_state:
    st.session_state["login"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""


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

    # =====================
    # LOGIN
    # =====================

    if pilihan == "Login":

        st.subheader("Login Pengguna")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Masuk"):

            try:
                db = koneksi()
                cursor = db.cursor()

                sql = """
                SELECT * FROM users
                WHERE username=%s AND password=%s
                """

                cursor.execute(sql, (username, password))
                hasil = cursor.fetchone()

                if hasil:
                    st.session_state["login"] = True
                    st.session_state["username"] = username

                    st.success("Login Berhasil!")
                    st.rerun()

                else:
                    st.error("Login Gagal! Periksa username dan password.")

                cursor.close()
                db.close()

            except Exception as e:
                st.error("Terjadi kesalahan:")
                st.error(str(e))


    # =====================
    # REGISTER
    # =====================

    elif pilihan == "Register":

        st.subheader("Pendaftaran Pengguna Baru")

        nama = st.text_input("Nama")
        username = st.text_input("Username Baru")
        password = st.text_input(
            "Password Baru",
            type="password"
        )

        if st.button("Daftar"):

            if nama and username and password:

                try:
                    db = koneksi()
                    cursor = db.cursor()

                    sql = """
                    INSERT INTO users (nama, username, password)
                    VALUES (%s, %s, %s)
                    """

                    cursor.execute(
                        sql,
                        (nama, username, password)
                    )

                    db.commit()

                    st.success("Register Berhasil!")

                    cursor.close()
                    db.close()

                except Exception as e:
                    st.error("Register Gagal:")
                    st.error(str(e))

            else:
                st.warning("Semua data harus diisi!")


# =====================
# HALAMAN MENU
# =====================

else:
    menu.tampilkan_menu()
