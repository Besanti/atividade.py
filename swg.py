import streamlit as st
import matplotlib.pyplot as plt

def main():
    # Dados do gráfico
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]

    # Criando o gráfico
    fig, ax = plt.subplots()
    ax.bar(x, y)

    # Personalizando o gráfico
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Gráfico de Barras')

    # Exibindo o gráfico usando o Streamlit
    st.pyplot(fig)

# Chamando a função principal
if __name__ == '__main__':
    main()
