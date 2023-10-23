import streamlit as st
import pandas as pd
import requests


# Leer el archivo CSV en un DataFrame
url = "https://raw.githubusercontent.com/JeronimoVasquez1307/prueba_login/main/usuarios.csv"
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
    # Actualizar el archivo CSV en GitHub
    df.to_csv("usuarios.csv", index=False, header=True)
      
    
     # Realizar una solicitud HTTP para cargar los datos actualizados en GitHub
    with open("usuarios.csv", "rb") as file:
        response = requests.put(url, data=file, headers={'Content-Type': 'application/octet-stream'})

    if response.status_code == 200:
        st.success("Usuario registrado con éxito y archivo actualizado en GitHub")
    else:
        st.error("Error al actualizar el archivo en GitHub")
   

# Mostrar los datos de usuario registrados en el archivo CSV
st.subheader("Usuarios Registrados")
st.write(df)
