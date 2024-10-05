import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st

#carregar os dados no dataframe
dados = pd.read_csv("houses_to_rent_v2.csv")
dados_para_analise = dados
st.write("""# Dashboard para apresentação do trabalho """)
st.write("""# Análise por filtros """)
# prepara as visualizações = filtros
st.sidebar.image("aluguel.jpeg")
#filtro por cidades
lista_cidades = st.sidebar.multiselect("Selecione a Cidade", ["São Paulo", "Porto Alegre", "Rio de Janeiro", "Campinas", "Belo Horizonte"])

#Filtros
#area
menor_area = 0
maior_area = 2000
intervalo_data_area = st.sidebar.slider("Area em M²",min_value=menor_area, max_value=maior_area,value=(menor_area, maior_area))

#filtro por salas
menor_sala= 1
maior_sala = 13
intervalo_data_sala = st.sidebar.slider("salas",min_value=menor_sala, max_value=maior_sala,value=(menor_sala, maior_sala))
#filtro por banheiros
menor_banheiro= 1
maior_banheiro = 10
intervalo_data_banheiro = st.sidebar.slider("Banheiros", min_value=menor_banheiro,max_value=maior_banheiro,value=(menor_banheiro, maior_banheiro))
#criação da tabela de dados
dados = dados.query("city in @lista_cidades")
dados = dados.query(f"area >= {intervalo_data_area[0]} and area <= {intervalo_data_area[1]}")
dados = dados.query(f"rooms >= {intervalo_data_sala[0]} and rooms <= {intervalo_data_sala[1]}")
dados = dados.query(f"bathroom >= {intervalo_data_banheiro[0]} and bathroom <= {intervalo_data_banheiro[1]}")
#Metricas
col1, col2, col3 = st.columns(3)
col1.metric("Preço médio da seleção", 'R$ {:.2f}'.format(dados['rent amount (R$)'].mean()))
col2.metric("Impostos médios da seleção", 'R$ {:.2f}'.format(dados['property tax (R$)'].mean()))
col3.metric("Média de seguro da seleção", 'R$ {:.2f}'.format(dados['fire insurance (R$)'].mean()))

grafico2 = alt.Chart(dados).mark_bar().encode(
    x='animal',
    y='count()',
    color=alt.value('blue'),
    tooltip=['animal', 'count()']
).properties(
    title='Aceitação de pets'
).interactive()

st.altair_chart(grafico2, use_container_width=True)




st.dataframe(dados)

#Analise dos totais 
st.write("""# Análise especifica de todos os dados """)
fig = px.scatter(dados_para_analise, x="city", y="total (R$)")
event = st.plotly_chart(fig, key="iris", on_select="rerun")


chart1 = alt.Chart(dados_para_analise).mark_bar().encode(
    x='city',
    y='count()',
    color=alt.value('blue'),
    tooltip=['city', 'count()']
).properties(
    title='Total por cidade'
).interactive()

st.altair_chart(chart1, use_container_width=True)

chart2 = alt.Chart(dados_para_analise).mark_bar().encode(
    x='animal',
    y='count()',
    color=alt.value('blue'),
    tooltip=['animal', 'count()']
).properties(
    title='Aceitação de pets'
).interactive()

st.altair_chart(chart2, use_container_width=True)
