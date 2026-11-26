import streamlit as st
import mysql.connector
import certifi

def koneksi():

    config = st.secrets["tidb"]

    db = mysql.connector.connect(
        host=config["host"],
        port=int(config["port"]),
        user=config["user"],
        password=config["password"],
        database=config["database"],
        ssl_ca=certifi.where(),
        ssl_verify_cert=True,
        ssl_verify_identity=True
    )

    return db
