import streamlit as st

st.title('Program Streamlit')
with st.form(key="my_form"):
    nama = st.text_input("Nama Lengkapmu")
    jenis_kelamin = st.radio("Jenis Kelaminmu", ("Laki-laki", "Perempuan"))
    submit = st.form_submit_button(label="Kirim")

# buat aktifin venv -> .\venv\Scripts\activate.ps1
# Deaktivasi venv -> deactivate


