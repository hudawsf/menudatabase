import streamlit as st
import pandas as pd
from database import koneksi

def tampilkan_menu():

    st.sidebar.title("☕ Aplikasi Kafe")

    pilihan = st.sidebar.selectbox(
        "Pilih Menu",
        ["Beranda", "Daftar Menu", "Tambah Menu", "Logout"]
    )

    # =========================
    # HALAMAN BERANDA
    # =========================
    if pilihan == "Beranda":

        st.title("Halaman Beranda")
        st.success("Selamat Datang, " + st.session_state["username"])

    # =========================
    # DAFTAR MENU
    # =========================
    elif pilihan == "Daftar Menu":

        st.title("Daftar Menu Kafe")

        try:
            db = koneksi()

            data = pd.read_sql("SELECT * FROM menu", db)

            st.dataframe(data, use_container_width=True)
            st.write("Jumlah Menu:", len(data))

            db.close()

        except Exception as e:
            st.error("Gagal mengambil data menu:")
            st.write(e)

    # =========================
    # TAMBAH MENU
    # =========================
    elif pilihan == "Tambah Menu":

        st.title("Tambah Menu Kafe")

        with st.form("form_tambah_menu"):

            nama_menu = st.text_input("Nama Menu")

            kategori = st.selectbox(
                "Kategori",
                ["Makanan", "Minuman", "Snack"]
            )

            harga = st.number_input(
                "Harga",
                min_value=0,
                step=1000
            )

            simpan = st.form_submit_button("Simpan Menu")

            if simpan:

                if nama_menu.strip() == "" or harga <= 0:
                    st.warning("Nama menu dan harga harus diisi!")

                else:
                    try:
                        db = koneksi()
                        cursor = db.cursor()

                        sql = """
                        INSERT INTO menu (nama_menu, kategori, harga)
                        VALUES (%s, %s, %s)
                        """

                        cursor.execute(
                            sql,
                            (nama_menu, kategori, int(harga))
                        )

                        db.commit()

                        cursor.close()
                        db.close()

                        st.success("Menu berhasil disimpan!")

                    except Exception as e:
                        st.error("Gagal menyimpan menu:")
                        st.write(e)

    # =========================
    # LOGOUT
    # =========================
    elif pilihan == "Logout":

        st.session_state["login"] = False
        st.session_state["username"] = ""

        st.rerun()
