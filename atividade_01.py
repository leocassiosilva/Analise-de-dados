# -*- coding: utf-8 -*-
"""Atividade 01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c3qtaynodTq5NvpPWcqaRHsUWTe9W_Dw

# Análise Exploratoria de dados
"""

from google.colab import drive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/metodos_quantitativos/Dados-Pesquisa.csv')

df.head()[0:100]

"""---

# INFORMAÇÔES E GRÁFICOS

**Tipo dos dados**
"""

df.dtypes[0:40]

"""---

# Soma dos número nulos
"""

df.isnull().sum()[0:40]

"""---

# Valores da coluna Age
"""

coluna_age = df['Age']

coluna_age[0:40]

#df.groupby(['Age']).Age.count().sort_values().plot(kind='pie')

plt.style.use("ggplot")
plt.figure(figsize = (30, 12))
df["Age"].hist(bins = 40, ec = "k", alpha = .6, color = "royalblue")
plt.title("Age")

"""---

# Quantidade de valores que se repete
"""

#Quantidade de valores que se repete usando o metodo do bandas counts
coluna_age.value_counts()

"""# Media da coluna Age

---
"""

#Fazendo a media dos dados da coluna Age
mean_df = df['Age'].mean()
print(mean_df)

"""---

"""

coluna_CityPopulation = df['CityPopulation']
coluna_CityPopulation[0:40]

"""---

# Contando quantas vezes um determinado valor se repete na coluna CityPopulation
"""

colunaCitypopulation = coluna_CityPopulation.value_counts()
colunaCitypopulation

colunaCitypopulation.plot.pie()

mean_df = colunaCitypopulation.mean()
print(mean_df)

"""---

# EmploymentStatus
"""

#EmploymentStatus
coluna_EmploymentStatus = df['EmploymentStatus']
coluna_EmploymentStatus[0:40]

colunaEmploymentStatus = coluna_EmploymentStatus.value_counts()
colunaEmploymentStatus
colunaEmploymentStatus.plot.bar(color='b')

"""---

# CommuteTime
"""

#CommuteTime
coluna_CommuteTime = df['CommuteTime']
coluna_CommuteTime

#colunaCommuteTime = coluna_CommuteTime.value_counts()
#colunaCommuteTime.plot.line()

plt.style.use("ggplot")
plt.figure(figsize = (20, 12))
df["CommuteTime"].hist(bins = 40, ec = "k", alpha = .6, color = "royalblue")
plt.title("CommuteTime")

df.groupby(['CommuteTime']).CommuteTime.count().sort_values()[1:].plot(kind='bar')

#ExpectedEarning
coluna_ExpectedEarning = df['ExpectedEarning']
coluna_ExpectedEarning

colunaExpectedEarning = coluna_ExpectedEarning.value_counts()
colunaExpectedEarning

"""# ExpectedEarning"""

coluna_ExpectedEarning = df['ExpectedEarning']
coluna_ExpectedEarning[0:20]

plt.style.use("ggplot")
plt.figure(figsize = (20, 12))
df["ExpectedEarning"].hist(bins = 40, ec = "k", alpha = .6, color = "royalblue")
plt.title("ExpectedEarning")

"""# HasDebt

"""

#HasDebt
df_total = df["HasDebt"] .sum()
df_total