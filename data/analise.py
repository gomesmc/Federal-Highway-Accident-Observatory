import pandas as pd

data_24 = pd.read_csv('raw/acidentes2024_todas_causas_tipos.csv', encoding = 'ISO-8859-1', sep= ';')

# -----------------------------------------
#VERIFICAÇÃO DE VALORES DO DATASET DE 2024
# -----------------------------------------

print('Dados dos acidentes em 2024\n')
print(f'\n{data_24.columns}') 
print(f'\nQuantidade de linhas: {data_24.shape[0]}')
print(f'\nQuantidade de colunas: {data_24.shape[1]}')
print(f'\nTipo do DataFrame: {type(data_24)}')
print(f'\nTipo das colunas:\n {data_24.dtypes}')

qtde_nulos = data_24.isna().sum().sum()
print(f'\nQuantidade de valores nulos no DataFrame: {qtde_nulos}')

qtde_vazios = data_24.eq('').sum().sum()
print(f'\nQuantidade de valores vazios no DataFrame: {qtde_vazios}')

# -----------------------------------------------------
# TRANSFORMAÇÃO DOS TIPOS DAS COLUNAS DO DATASET DE 2024
# -----------------------------------------------------

data_24['data_inversa'] = pd.to_datetime(data_24['data_inversa'])
data_24['horario'] = pd.to_datetime(data_24['horario'])

data_24['km'] = data_24['km'].str.replace(',', '.')
data_24['km'] = data_24['km'].astype('Float64') 

data_24['br'] = pd.to_numeric(data_24['br'], errors = 'coerce').astype('Float64')

data_24['br'] = pd.to_numeric(data_24['br'], errors='coerce').astype('Int64')

data_24['ano_fabricacao_veiculo'] = pd.to_numeric(data_24['ano_fabricacao_veiculo'], errors='coerce').astype('Int64')

print(f'\n Tipo do DataSet 2024 corrigido: \n{data_24.dtypes}')

# -----------------------------------------
# VERIFICAÇÃO DE VALORES DO DATASET DE 2025
# -----------------------------------------

data_25 = pd.read_csv('raw/acidentes2025_todas_causas_tipos.csv', encoding = 'ISO-8859-1', sep = ';')

print('\nDados dos acidentes em 2025\n')
print(f'{data_25.columns}')
print(f'\nQuantidade de linhas: {data_25.shape[0]}')
print(f'\nQuantidade de colunas: {data_25.shape[1]}')
print(f'\nTipo do DataFrame: {type(data_25)}')
print(f'\nTipo das colunas:\n {data_25.dtypes}')

qtde_nulos = data_25.isna().sum().sum()
print(f'\nQuantidade de valores nulos no DataFrame: {qtde_nulos}')

qtde_vazios = data_25.eq('').sum().sum()
print(f'\nQuantidade de valores vazios no DataFrame: {qtde_vazios}')

# -----------------------------------------------------
# TRANSFORMAÇÃO DOS TIPOS DAS COLUNAS DO DATASET DE 2025
# -----------------------------------------------------

data_25['data_inversa'] = pd.to_datetime(data_25['data_inversa'])

data_25['horario'] = pd.to_datetime(data_25['horario'])

data_25['km'] = data_25['km'].str.replace(',', '.')
data_25['km'] = data_25['km'].astype('Float64') 

data_25['br'] = pd.to_numeric(data_25['br'], errors = 'coerce').astype('Float64')

data_25['ano_fabricacao_veiculo'] = pd.to_numeric(data_25['ano_fabricacao_veiculo'], errors='coerce').astype('Int64')

print(f'\n Tipo do DataSet 2025 corrigido: \n{data_25.dtypes}')