import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
valor = st.number_input("Valor")

if modo == "Celsius a Fahrenheit":
    resultado = celsius * 9 / 5 + 32
    st.success(f"**{round(resultado, 2)} ºF**")
    st.caption(f"{valor} ºC convertidos a Fahrenheit")
else: 
    resultado = (valor - 32) * 5 / 9
    st.success(f"**{round(resultado, 2)} ºC**")
    st.caption(f"{valor} ºF convertidos a Celsius")