import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"])
valor = st.number_input("Valor")

if modo == "Celsius a Fahrenheit":
    resultado = celsius * 9 / 5 + 32
    st.write(f"{valor} ºC son {round(resultado, 2)} ºF")
elif modo == "Fahrenheit a Celsius": 
    resultado = (valor - 32) * 5 / 9
    st.write(f"{valor} ºF son {round(resultado, 2)} ºC")
elif modo == "Celsius a Kelvin":
    resultado = valor + 273.15
    st.write(f"{valor} ºC son {round(resultado, 2)} K")
elif modo == "Kelvin a Celsius":
    resultado = valor - 273.15
    st.write(f"{valor} K son {round(resultado, 2)} ºC")
