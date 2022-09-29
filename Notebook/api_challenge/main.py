#!/usr/bin/env python
# coding: utf-8
from gettext import install

# In[1]:

from fastapi import FastAPI

import pandas as pd

import pickle

from sklearn.compose import _column_transformer


# In[2]:


app = FastAPI()


# In[3]:

with open('../Modelo/onehot_AluraCash.pkl', 'rb') as file:
       onehot_encoder = pickle.load(file)

with open('../Modelo/Scaler_AluraCash.pkl', 'rb') as file:
       scaler = pickle.load(file)

with open('../Modelo/modelo_AluraCash.pkl','rb') as file:
       modelo = pickle.load(file)

# In[5]:


@app.get('/modelo/v1={Idade}&v2={Salario_anual}&v3={Situacao_prop}&v4={Tempo_trabalho}&v5={Motivo_emprest}&v6={Pont_emprest}&v7={Total_emprest}&v8={Tx_juros}&v9={Renda_pecentual}&v10={Periodo}&v11={Inadimplente}')

def previsao(Idade, Salario_anual, Situacao_prop,
             Tempo_trabalho, Motivo_emprest, Pont_emprest,
             Total_emprest, Tx_juros, Renda_pecentual, Periodo, Inadimplente):


    dados = {'Idade':[int(Idade)],
             'Salario_anual':[int(Salario_anual)],
             'Situacao_prop':[str(Situacao_prop)],
             'Tempo_trabalho':[int(Tempo_trabalho)],
             'Motivo_emprest':[str(Motivo_emprest)],
             'Pont_emprest':[str(Pont_emprest)],
             'Total_emprest':[float(Total_emprest)],
             'Tx_juros':[float(Tx_juros)],
             'Renda_pecentual':[float(Renda_pecentual)],
             'Periodo':[int(Periodo)],
             'Inadimplente':[int(Inadimplente)]}

    dados = pd.DataFrame(dados)

    dados = onehot_encoder.transform(dados)
    dados_enc = pd.DataFrame(dados, columns = onehot_encoder.get_feature_names_out())

    dados_transf = scaler.transform(dados_enc)
    dados_transf = pd.DataFrame(dados_transf, columns = onehot_encoder.get_feature_names_out())

    return{'Resultado':modelo.predict(dados_transf).tolist()[0],
           'Probabilidade_0':modelo.predict_proba(dados_transf).tolist()[0][0],
           'Probabilidadte_1':modelo.predict_proba(dados_transf).tolist()[0][1]}
    
                     
