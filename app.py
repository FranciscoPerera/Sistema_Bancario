import streamlit as st

# Estado da aplicação
if "saldo" not in st.session_state:
    st.session_state.saldo = 0

if "extrato" not in st.session_state:
    st.session_state.extrato = []

if "saques" not in st.session_state:
    st.session_state.saques = 0

LIMITE_SAQUES = 3
LIMITE_SAQUE = 500

# TÍTULO
st.title("Banco Digital")

st.divider()

# MENU
opcao = st.selectbox(
    "Escolha uma operação",
    ["Depósito", "Saque", "Extrato"]
)

# DEPÓSITO
if opcao == "Depósito":
    valor = st.number_input("Digite o valor do depósito", min_value=0.0, step=10.0)

    if st.button("Depositar"):

        if valor > 0:
            st.session_state.saldo += valor
            st.session_state.extrato.append(f"Depósito: R$ {valor:.2f}")
            st.success("Depósito realizado com sucesso!")
        else:
            st.error("Valor inválido")

# SAQUE
elif opcao == "Saque":
    valor = st.number_input("Digite o valor do saque", min_value=0.0, step=10.0)

    if st.button("Sacar"):
        
        if valor <= 0:
            st.error("Valor inválido")
        elif valor > st.session_state.saldo:
            st.error("Saldo insuficiente")
        elif valor > LIMITE_SAQUE:
            st.error("Limite por saque é R$ 500")
        elif st.session_state.saques >= LIMITE_SAQUES:
            st.error("Limite diário de saques atingido")
        else:
            st.session_state.saldo -= valor
            st.session_state.extrato.append(f"Saque: R$ {valor:.2f}")
            st.session_state.saques += 1
            st.success("Saque realizado com sucesso!")

# EXTRATO
elif opcao == "Extrato":
    st.subheader("Extrato")

    if len(st.session_state.extrato) == 0:
        st.warning("Nenhuma movimentação")
    else:
        for item in st.session_state.extrato:
            st.write(item)

    st.divider()
    st.write(f"Saldo atual: R$ {st.session_state.saldo:.2f}")