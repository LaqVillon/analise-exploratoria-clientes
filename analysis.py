import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Leitura de dados em csv
dados = pd.read_csv('dataset/amostra_banco_distrito.csv', decimal=',') 

# Tabela de frequências absolutas por tipo de empresa
tab = pd.crosstab(index=dados['Empresa'], columns='Frequência')

# --------------------------------------- Figuras -----------------------------------------
# Estilo
sns.set_style("darkgrid")

# # Gráfico pizza de frequências por tipo de empresa
# plt.rcParams["figure.figsize"] = [5,5]
# plot = tab.plot.pie(y='Frequência',autopct='%1.1f%%', startangle = 0, 
#                     fontsize=16.0, textprops=dict(color="w"))
# plt.savefig("figuras/pizza-frequencia-empresa.jpg")
# plt.clf()

# # Salario por sexo e empresa em boxplot
# plt.rcParams["figure.figsize"] = [6.5, 5]
# sns.boxplot(data=dados, y='Salario', x='Empresa', hue='Sexo', palette='pastel', 
#             flierprops=dict(marker='o', markerfacecolor='black', markersize=4, markeredgecolor='none'),
#             meanprops=dict(linestyle='--', linewidth=1.5, color='black'), meanline=True, showmeans=True)
# plt.yticks()
# plt.xlabel('Tipo de Empresa', fontsize = 12)
# plt.ylabel('Salário', fontsize = 12)
# plt.legend(title='Sexo', title_fontsize=12, loc='best', fontsize='large')
# plt.savefig("figuras/salario-sexo-empresa.jpg")
# plt.clf()

# Salario por sexo, empresa e distrito em boxplot
media_distrito = dados.groupby(['Distrito'])['Salario'].mean().sort_values(ascending=False)
plt.rcParams["figure.figsize"] = [19.5, 16]
sns.boxplot(data=dados, y='Distrito', x='Salario', hue='Sexo', palette='pastel', 
            order=media_distrito.index)
plt.xlabel('Salário', fontsize = 20)
plt.xticks(fontsize = 18)
plt.legend(title='Sexo', title_fontsize=16, loc='best', fontsize='xx-large')
plt.savefig("figuras/salario-sexo-distrito.jpg")
plt.clf()

# Distribuição dos dados idade, salário e tipo de empresa
plt.figure(figsize=(20,20))
sns.jointplot(data=dados, x='Idade', y='Salario',  hue='Empresa', height=6)
plt.savefig("figuras/distribuicao-idade-salario.jpg")
plt.tight_layout()
plt.clf()

# Associação Salario - idade - empresa - sexo
sns.lmplot(x='Idade', y='Salario', hue='Sexo', col='Empresa',  data=dados, 
           height=5, aspect=0.5, ci=90)
plt.tight_layout()
plt.savefig("figuras/associacao-salario-idade-empresa-sexo.jpg")
plt.clf()

# Associação entre variáveis quantitativas
dados_nozeros = dados[dados['Saldo_investimento']*dados['Saldo_poupança']!=0]
sns.pairplot(dados_nozeros[['Salario','Saldo_cc', 'Saldo_poupança', 'Saldo_investimento']], kind='reg')
plt.tight_layout()
plt.savefig("figuras/associacao-variaveis-quantitativas.jpg")
plt.clf()
