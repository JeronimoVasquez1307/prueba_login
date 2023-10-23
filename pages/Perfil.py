import streamlit as st


st.title("Perfil de Usuario")

# Aquí puedes obtener y mostrar información del perfil del usuario
nombre = st.session_state
email = "usuario@example.com"
edad = 30
juegos_favoritos = ["Juego 1", "Juego 2", "Juego 3"]

st.write(f"**Nombre:** {nombre}")
st.write(f"**Email:** {email}")
st.write(f"**Edad:** {edad} años")
st.write("**Juegos Favoritos:**")
st.write(juegos_favoritos)

# Puedes agregar más contenido relacionado con el perfil aquí


