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
    url = "https://api.github.com/repos/JeronimoVasquez1307/prueba_login/contents/usuarios.csv"
    data = {"content": df.to_csv(index=False).encode("utf-8")}
    response = requests.put(url,data=data)
    st.success("Usuario registrado con éxito")
   

# Mostrar los datos de usuario registrados en el archivo CSV
st.subheader("Usuarios Registrados")
st.write(df)
