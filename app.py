import streamlit as st
from plot.interactive import plot_line_i

st.title('Stock price App')

#sidebear
st.sidebar.header('User Input')
symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')
st.write(symbol)

#plot
fig = plot_line_i(symbol)
st.plotly_chart(fig)