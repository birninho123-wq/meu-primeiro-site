import streamlit as st 

st.title("CADASTRO")
st.subheader("Preencha os campos abaixo para se cadastrar")
nome = st.text_input("nome ou apelido")
idade = st.slider_input("idade" , 0  , 120)
email = st.text_input("email")
senha = st.text_input("senha", type="password")
if st.button("Cadastrar"):
    st.success("Cadastro realizado com sucesso!")

