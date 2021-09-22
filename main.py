import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""O Objetivo é realizar a leitura de duas cotações sendo Ibovespa Futuro e Dolar, para entendimento da relação entre si"""
"""O Periodo de análise será entre 20 de agosto á 20 de setembro"""
#Importação dos Datasets
bolsa_valores = pd.read_csv('IBOV.csv')
dollar = pd.read_csv('USD_BRL.csv')
# Leitura do Dataset completo da Cotação do Dollar e da bolsa de valores 
print("\n\n 1° Passo: Leitura do dataframe completo")
print(f"Tabela USD/BRL \n {dollar}")
print(f"Tabela IBOVESPA \n {bolsa_valores}\n")
"""Filtro para leitura somente da data de 20 de agosto a 20 de setembro de 2021."""
"""Dolar"""
print("\n\nTABELA DOLAR USD/BRL \n")
#df_inverte_tab_dollar = dollar.tail(31)
#tab_dol_mes = df_inverte_tab_dollar.loc[239:260]
dollar.set_index('Date', inplace=True)
tab_dol_mes = dollar.loc['2021-08-20':'2021-09-2021']
print(tab_dol_mes)
"""Ibovespa"""
print("\n\nTABELA IBOVESPA\n")
#df_inverte_tab_bovespa = bolsa_valores.tail(31)
#tab_ibo_mes = df_inverte_tab_bovespa.loc[225:245]
bolsa_valores.set_index('Date', inplace=True)
tab_ibov_mes = bolsa_valores.loc['2021-08-20':'2021-09-2021']
print(tab_ibov_mes)
"""Filtrando o dataframe disponibilizando apenas os dados que serão utilizados"""
"""Dolar"""
tab_dol_mes.drop(['Open','High','Low','Adj Close','Volume'],axis=1,inplace=True)
tab_dol_mes.head()
print(tab_dol_mes)
"""Ibovespa"""
tab_ibov_mes.drop(['Open', 'High', 'Low', 'Adj Close','Volume'], axis=1, inplace=True)
tab_ibov_mes.head()
print(tab_ibov_mes)
"""Juntando dados de duas tabelas para realizar a relação entre o Valor do Dolar e a Vaariação da Bolsa de Valores"""
merge_dados = tab_dol_mes.merge(tab_ibov_mes, how='inner',left_on='Date', right_on='Date')
print(merge_dados)
"""Geração do Gráfico de disperção para Análise de Relação entre Ativos"""
merge_dados.plot(x='Close_y', y='Close_x', kind='scatter')
plt.show()
