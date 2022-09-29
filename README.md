![68747470733a2f2f692e696d6775722e636f6d2f6f7861623375752e706e67](https://user-images.githubusercontent.com/107072611/193137825-545344ad-260c-4057-9e39-d7ab037a045c.png)

# Alura_Cash - 2° Challenge de Dados Alura.

## Contextualização.
Fui contratado como pessoa de dados pelo banco digital **Alura Cash** a fim de reduzir a inadimplencia entre os clientes. Segundo a diretoria financeira, esses eventos vem crescendo dentre eles após liberação de crédito.

Desse modo e com a finalidade de mitigar a perca de capital ocasionada por esses clientes, solicitei o histórico de crédito, o histórico de solicitação de empréstimos e outras informações financeiras. A ideia é desenvolver um modelo, com base nas características e informações presentes nos dados que nos foram oferecidos, que seja capaz de identificar aqueles clientes que poderão vir a se tornar inadimplentes e solucionar o problema enfretado pelo banco.

## Etapas de desenvolvimento do projeto.
### Análise e tratamento dos dados. 
Os dados solicitados estavam contidos em um banco de dados, que nos foi disponibilizado em forma de [dumps](https://github.com/MateusSampaio1/Alura_Cash/tree/main/Dados/Dump). Depois de acessá-los foi necessário identificar se as informações solicitadas anteriormente estavam presentes nas tabelas do banco, observar as características destes dados, verificar se existiam algum problema, inconsistência e/ou ausência de dados.

Essa é uma parte fundamental para o desenvolvimento das etapas seguintes, visto que uma vez identificada alguma inconsistência, basta tratá-la antes de prosseguir para a parte de modelagem destes dados.

Na parte de modelagem, as tabelas foram unidas, após definição das chaves primárias e estrangeiras,  com o auxílio do **Join** entre as tabelas, permitindo a criação de um dataset que foi utilizado para a criação dos modelos de classificação.

O script com todo o desenvolvimento descrito acima pode ser encontrado na pasta [SQL_Scripts](https://github.com/MateusSampaio1/Alura_Cash/tree/main/SQL_Scripts), vale ressaltar que o SGBD utilizado foi o **MySQL**. 

### Criação dos modelos de classificação.
Após a formação e exportação do dataset, foram utilizadas algumas bibliotecas e ferramentas de ciência de dados como **Pandas**, **Seaborn**, **Matplotlib**, **Numpy**, **Scikit Learn**  dentre outras, para um tratamento mais refinado destes dados antes da parte de criação dos modelos. 

De início foram realizados alguns processos de tratamento das linhas que estavam vazias, os registros que tinham linhas nulas na coluna **target(Possib_inadimp)** ou em colunas qualitativas foram removidos, os demais foram tratados por meio da substituição da média ou mediana.

Em seguida foram removidos os registros que estavam muito fora da realidade e se caracterizavam como Outlier, como por exemplo clientes que possuíam mais de 120 anos de idade ou de tempo de trabalho.

Uma vez finalizado esses tratamentos, foram realizados o processo de encoding das variáveis qualitativas, verificado as correlações das variáveis presentes no dataset, normalização das features com o **Standard Scaler**,  e o balanceamento dos dados com o **SMOTE**.

Posteriormente foram criados os modelos de classificação, neste projeto foram utilizados o **Dummy**, **Decision Tree**, **Random Forest** e o **Gradient Boosting**. Destes, o que apresentou o melhor desempenho, mesmo após otimização, foi o GradientBoosting. Apresentando uma **roc_auc_score média de pouco mais de 97%** e mostrando que o modelo criado é capaz de distinguir bem entre os possíveis clientes inadimplentes e o não inadimplentes. 

O desenvolvimento desta etapa do projeto pode ser encontrada na pasta [Notebook](https://github.com/MateusSampaio1/Alura_Cash/tree/main/Notebook) com o nome de [AluraCash_ML](https://github.com/MateusSampaio1/Alura_Cash/blob/main/Notebook/AluraCash_ML.ipynb).

### Criação da API e Dashboard.
Na etapa seguinte deste projeto e logo depois da criação e validação do modelo de classificação, foi criada um API(Application Programming Interface) que nos permitirá realizar uma requisão para o nosso modelo diretamente do Power Bi.

O primeiro passo foi a criação e disponibilização da API, foi necessário criar um [script](https://github.com/MateusSampaio1/Alura_Cash/blob/main/Notebook/api_challenge/main.py) em Python que nos permite receber as informações de um novo cliente, realizar os tratamentos necessários e rodar o modelo treinado para efetuar uma predição. Neste processo foram utilizados o FastAPI e o Uvicorn, um para criação da aplicação e o outro para rodá-la localmente, permitindo assim que as request e response sejam realizadas.

Em seguida, bastou apenas realizar a "ligação" do Power Bi e desta aplicação através da **URL(Web)**. Vale ressaltar que para ser possível efetuar as novas consultas ao modelo, direto do dashboard, foram criados parâmetros que possibilitam inserir novos dados a URL e assim realizar as predições.

Por fim, foram analizados alguns [dados](https://github.com/MateusSampaio1/Alura_Cash/blob/main/Dados/Dados_tratados.csv) presentes na base de dados já tratadas e criado um [Dashboard](https://github.com/MateusSampaio1/Alura_Cash/blob/main/Dashboard_AluraCash.pbix).


