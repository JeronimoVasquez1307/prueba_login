import streamlit as st
import pandas as pd
from pages import Perfil


# Crear el DataFrame
df = pd.read_csv("usuarios.csv")

# Título de la aplicación
st.title("Login")

# Formulario de login
usuario = st.text_input("Usuario")
contrasena = st.text_input("Contraseña", type="password")

if st.button("Iniciar sesión"):
    if df["Usuario"].str.contains(usuario).any() and df['Contraseña'].str.contains(contrasena).any():
        st.success("Inicio de sesión exitoso")
        st.session_state = usuario
   
    else:
        st.error("Usuario o contraseña incorrectos")


