import pandas as pd

# criação do dataset de transações
lista = [[1,3545,3000,6.99],[2,3545,4500,0.45],[3,3509,69998,0],[4,3510,1,None],[5,4510,34,40]]
df_transacoes = pd.DataFrame(lista, columns = ['transaction_id', 'client_id', 'total_amount', 'discount_percentage'])

df_transacoes["valor_liquido"] = df_transacoes["total_amount"] - df_transacoes["total_amount"] * (df_transacoes["discount_percentage"] / 100 ).fillna(0)

# criação do dataset de contratos
lista = [[3,3545,'Magazine Luana',2.00,'true'],[4,3545,'Magazine Luana',1.95,'false'],[5,3509,'Lojas Italianas',1,'true'],[6,3510,'Carrerfive',3.00,'true']]
df_contratos = pd.DataFrame(lista, columns = ['contract_id', 'client_id', 'client_name', 'percentage', 'is_active'])

# criação do dataset com o valor líquido por transação e cliente
df_transacoes_filtrado = df_transacoes[['total_amount', 'client_id', 'valor_liquido']].fillna(0)

# criação do dataset com as porcentagens por cliente e já filtrando apenas os contratos ativos
df_contratos_filtrado = df_contratos[['client_id','percentage', 'is_active']].loc[df_contratos['is_active'] == 'true']

# junção dos dataframes de transações e contratos já com a regra de negócio aplicada para cálculo do ganho total
join_df = pd.merge(df_transacoes_filtrado, df_contratos_filtrado, on="client_id", how="left")

join_df["ganho_total"] = join_df["valor_liquido"] * (join_df["percentage"] / 100 )

# resultado esperado - ganho total da Acquirer LTDA
resultado = join_df['ganho_total'].sum()
print(f'O ganho total da Acquirer LTDA é de: R$',resultado.round(3))
