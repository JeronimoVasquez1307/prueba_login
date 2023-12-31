import streamlit as st
import pandas as pd
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configura las credenciales
credenciales = 'baseusuarios-402906-cb3c6dfcc470.json'
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credenciales, scope)
gc = gspread.authorize(credentials)
# Leer el archivo CSV en un DataFrame
# Abre la hoja de Google Sheets por su URL
gc_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTAfp6uFRC6PylYstGVXoXaEiXv8TTqS3BFcx_wVJ-BfQOILj9OUluNgQQx4Ba4-kujstzHgF71Pv6-/pubhtml"
worksheet = gc.open_by_url(gc_url).usuarios
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTAfp6uFRC6PylYstGVXoXaEiXv8TTqS3BFcx_wVJ-BfQOILj9OUluNgQQx4Ba4-kujstzHgF71Pv6-/pubhtml"
df = pd.read_csv(url)

# Título de la aplicación
st.title("Registro de Usuarios")

# Formulario para recopilar información de usuario
usuario = st.text_input("Usuario")
contrasena = st.text_input("Contraseña", type="password")
nombre = st.text_input("Nombre")
correo = st.text_input("Correo electrónico")

if st.button("Registrar"):
    # Agregar la nueva fila al archivo CSV
    nueva_fila = {
        "Usuario": usuario,
        "Contraseña": contrasena,
        "Nombre": nombre,
        "Correo electrónico": correo
    }
    nuevo_df = pd.DataFrame([nueva_fila])
    df = pd.concat([df, nuevo_df], ignore_index=True)
    
    # Actualizar la hoja de Google Sheets con los datos actualizados
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    st.success("Usuario registrado con éxito y archivo actualizado en Google Sheets")
      
    
    

# Mostrar los datos de usuario registrados en el archivo CSV
st.subheader("Usuarios Registrados")
st.write(df)
