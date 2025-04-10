import streamlit as st
import pandas as pd
import numpy as np
np.random.seed(123456)
import matplotlib.pyplot as plt

from decimal import Decimal
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
import plotly.graph_objects as go
pd.options.display.max_columns = 200

st.set_page_config(layout="wide")

df = pd.read_csv('questionario_escolas.csv')
df0 = df.rename(columns={'index':'index',
 'Carimbo de data/hora':'data/hora',
 'Escola que estuda:':'escola',
 'Cidade que reside':'cidade',
 'Sua idade':'idade',
 'Ano escolar (série)':'ano',
 'Você tem interesse em fazer um Curso Superior?':'curso',
 'Qual curso superior você tem interesse?':'curso',
 'Marque qual motivação pessoal você tem para fazer um Curso Superior: ':'motivacao',
 'Marque abaixo a opção que possa explicar sua escolha: (permitido marcar mais de uma opção)':'explicar',
 'Você sabia que a Universidade Federal de Viçosa (UFV) possui um campus no município de Florestal-MG?  ':'sabia',
 'No campus da UFV, em Florestal-MG, são oferecidos GRATUITAMENTE 10 Cursos Superiores (listados abaixo). Se você tivesse que escolher um deles, qual seria?':'qual',
 'No campus UFV Florestal, os estudantes possuem diversas oportunidades para permanência no curso e desenvolvimento profissional e pessoal. Conhecendo essas oportunidades, marque para cada uma o grau de importância que elas teriam na sua escolha em fazer um curso superior no campus (sendo 1 não importante e 5 extremamente importante). [Auxílio financeiro para moradia]':'a1',
 'No campus UFV Florestal, os estudantes possuem diversas oportunidades para permanência no curso e desenvolvimento profissional e pessoal. Conhecendo essas oportunidades, marque para cada uma o grau de importância que elas teriam na sua escolha em fazer um curso superior no campus (sendo 1 não importante e 5 extremamente importante). [Auxílio financeiro para alimentação]':'a2',
 'No campus UFV Florestal, os estudantes possuem diversas oportunidades para permanência no curso e desenvolvimento profissional e pessoal. Conhecendo essas oportunidades, marque para cada uma o grau de importância que elas teriam na sua escolha em fazer um curso superior no campus (sendo 1 não importante e 5 extremamente importante). [Remuneração em projetos de pesquisa]':'a3',
 'No campus UFV Florestal, os estudantes possuem diversas oportunidades para permanência no curso e desenvolvimento profissional e pessoal. Conhecendo essas oportunidades, marque para cada uma o grau de importância que elas teriam na sua escolha em fazer um curso superior no campus (sendo 1 não importante e 5 extremamente importante). [Remuneração em projetos desenvolvidos com a comunidade externa]':'a4',
 'No campus UFV Florestal, os estudantes possuem diversas oportunidades para permanência no curso e desenvolvimento profissional e pessoal. Conhecendo essas oportunidades, marque para cada uma o grau de importância que elas teriam na sua escolha em fazer um curso superior no campus (sendo 1 não importante e 5 extremamente importante). [Remuneração em atividades administrativas na Universidade]':'a5',
 'No campus UFV Florestal, os estudantes possuem diversas oportunidades para permanência no curso e desenvolvimento profissional e pessoal. Conhecendo essas oportunidades, marque para cada uma o grau de importância que elas teriam na sua escolha em fazer um curso superior no campus (sendo 1 não importante e 5 extremamente importante). [Remuneração para monitores e tutores]':'a6',
 'No campus UFV Florestal, os estudantes possuem diversas oportunidades para permanência no curso e desenvolvimento profissional e pessoal. Conhecendo essas oportunidades, marque para cada uma o grau de importância que elas teriam na sua escolha em fazer um curso superior no campus (sendo 1 não importante e 5 extremamente importante). [Contato com empresas para estágio]':'a7',
 'Caso a UFV-Florestal oferecesse gratuitamente um curso preparatório para participar do processo seletivo para o ensino superior, você participaria?':'preparatorio',
 'A partir deste ano a UFV irá oferecer o processo seletivo seriado para os alunos do 1 ano do ensino médio. Você teria interesse em participar? (Apenas alunos do 1º ano devem responder!)':'seriado',
 'Você teria interesse em receber mais informações a respeito dos cursos e oportunidades oferecidas no Campus da UFV Florestal? Caso sim, por favor, escreva aqui seu contato (e-mail ou telefone):':'contato'})


df2=df0[df0["qual"].str.contains('Matemática', na=False)]
pd.set_option('display.max_rows', None)
df3=df2[df2["contato"].notnull()]
df3 = df3.reset_index()

grouped_df = df0.groupby(["cidade","sabia"]).size().reset_index(name="Count")
dfa = pd.DataFrame(grouped_df)
dfa=dfa.pivot(index='sabia', columns='cidade', values='Count')
dfa["index"] = dfa.index

st.title("Visão Geral")


st.dataframe(dfa)

cols = st.columns([1, 1, 1])

with cols[0]:
 medal_type = st.selectbox('Cidade', ['Betim', 'Florestal', 'Pará de Minas','Igarapé','Juatuba','Mateus Leme','Igaratinga','São Joaquim de Bicas','São José da Varginha','Pequi'])

 fig = px.pie(dfa, values=medal_type, names='index',
              title=f'A cidade {medal_type} conhece o campus',
              height=150, width=100)
 fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
 fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
 st.plotly_chart(fig, use_container_width=True)

with cols[1]:
 medal_type = st.selectbox('Cidade',
                           ['Florestal','Betim', 'Pará de Minas', 'Igarapé', 'Juatuba', 'Mateus Leme', 'Igaratinga',
                            'São Joaquim de Bicas', 'São José da Varginha','Pequi'])

 fig = px.pie(dfa, values=medal_type, names='index',
              title=f'A cidade {medal_type} conhece o campus',
              height=160, width=110)
 fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
 fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
 st.plotly_chart(fig, use_container_width=True)

with cols[2]:
 medal_type = st.selectbox('Cidade',
                           ['Pará de Minas','Florestal','Betim', 'Igarapé', 'Juatuba', 'Mateus Leme', 'Igaratinga',
                            'São Joaquim de Bicas', 'São José da Varginha','Pequi'])

 fig = px.pie(dfa, values=medal_type, names='index',
              title=f'A cidade {medal_type} conhece o campus',
              height=160, width=110)
 fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
 fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
 st.plotly_chart(fig, use_container_width=True)

with st.container():
    cols = st.columns([1, 1, 1])
    with cols[0]:
        medal_type = st.selectbox('Cidade', ['Juatuba','Betim', 'Florestal', 'Pará de Minas', 'Igarapé', 'Mateus Leme',
                                             'Igaratinga', 'São Joaquim de Bicas', 'São José da Varginha', 'Pequi'])

        fig = px.pie(dfa, values=medal_type, names='index',
                     title=f'A cidade {medal_type} conhece o campus',
                     height=150, width=100)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
        st.plotly_chart(fig, use_container_width=True)

    with cols[1]:
        medal_type = st.selectbox('Cidade',
                                  ['Igarapé','Florestal', 'Betim', 'Pará de Minas', 'Juatuba', 'Mateus Leme',
                                   'Igaratinga',
                                   'São Joaquim de Bicas', 'São José da Varginha', 'Pequi'])

        fig = px.pie(dfa, values=medal_type, names='index',
                     title=f'A cidade {medal_type} conhece o campus',
                     height=160, width=110)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
        st.plotly_chart(fig, use_container_width=True)

    with cols[2]:
        medal_type = st.selectbox('Cidade',
                                  [ 'Mateus Leme','Pará de Minas', 'Florestal', 'Betim', 'Igarapé', 'Juatuba',
                                   'Igaratinga',
                                   'São Joaquim de Bicas', 'São José da Varginha', 'Pequi'])

        fig = px.pie(dfa, values=medal_type, names='index',
                     title=f'A cidade {medal_type} conhece o campus',
                     height=160, width=110)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    cols = st.columns([1, 1, 1])
    with cols[0]:
        medal_type = st.selectbox('Cidade', ['Igaratinga','Juatuba','Betim', 'Florestal', 'Pará de Minas', 'Igarapé', 'Mateus Leme', 'São Joaquim de Bicas', 'São José da Varginha', 'Pequi'])

        fig = px.pie(dfa, values=medal_type, names='index',
                     title=f'A cidade {medal_type} conhece o campus',
                     height=150, width=100)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
        st.plotly_chart(fig, use_container_width=True)

    with cols[1]:
        medal_type = st.selectbox('Cidade',
                                  ['São Joaquim de Bicas','Igarapé','Florestal', 'Betim', 'Pará de Minas', 'Juatuba', 'Mateus Leme',
                                   'Igaratinga', 'São José da Varginha', 'Pequi'])

        fig = px.pie(dfa, values=medal_type, names='index',
                     title=f'A cidade {medal_type} conhece o campus',
                     height=160, width=110)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
        st.plotly_chart(fig, use_container_width=True)

    with cols[2]:
        medal_type = st.selectbox('Cidade',
                                  [ 'São José da Varginha', 'Mateus Leme','Pará de Minas', 'Florestal', 'Betim', 'Igarapé', 'Juatuba',
                                   'Igaratinga',
                                   'São Joaquim de Bicas', 'Pequi'])

        fig = px.pie(dfa, values=medal_type, names='index',
                     title=f'A cidade {medal_type} conhece o campus',
                     height=160, width=110)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    cols = st.columns([1, 1, 1])
    with cols[0]:
        medal_type = st.selectbox('Cidade', ['Pequi','Igaratinga','Juatuba','Betim', 'Florestal', 'Pará de Minas', 'Igarapé', 'Mateus Leme', 'São Joaquim de Bicas', 'São José da Varginha'])

        fig = px.pie(dfa, values=medal_type, names='index',
                     title=f'A cidade {medal_type} conhece o campus',
                     height=150, width=100)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        fig.update_traces(marker=dict(colors=['#e74c3c', '#3498db']))
        st.plotly_chart(fig, use_container_width=True)

