import tabula
import pandas as pd
from IPython.display import display 
import numpy as np



arquivo = tabula.read_pdf("edp.pdf", pages="1", multiple_tables=True)

# Quantidade de tabelas encontradas
print('Quantidade de tabelas na página: ', len(arquivo))
print("A")

# Filtra a tabela desejada com base no cabeçalho específico
tabela_desejada = None
for tabela in arquivo:
    if isinstance(tabela, pd.DataFrame) and not tabela.empty:
        # Verifica se a primeira linha da tabela contém o cabeçalho esperado
        if any("CCI DESCRIÇÃO DO PRODUTO" in str(cell) for cell in tabela.iloc[0]):
            tabela_desejada = tabela
            break

# Exibe a tabela desejada, se encontrada
if tabela_desejada is not None:
    tabela_desejada.columns = tabela_desejada.iloc[0]
    tabela_desejada[['CCI', 'DESCRIÇÃO DO PRODUTO']] = tabela_desejada["CCI DESCRIÇÃO DO PRODUTO"].str.split(" ", n=1, expand=True)
    
    tabela_desejada[["TARIFA APLICADA", "VALOR FORNEC", "TARIFA C/ IMPOSTOS", "B. CÁLC ICMS"]] = tabela_desejada["TARIFA VALOR TARIFA C/ B.CÁLC"].str.split(" ", n=3, expand=True)

    # Encontra o índice do "Itens financeiros"
    idx_itens_financeiros = tabela_desejada[tabela_desejada["CCI DESCRIÇÃO DO PRODUTO"].str.contains("ITENS FINANCEIROS", na=False)].index[0]
    # Criar a nova coluna "ITENS FINANCEIROS" com os valores abaixo dessa linha
    tabela_desejada['ITENS FINANCEIROS'] = tabela_desejada.loc[idx_itens_financeiros + 1:, 'CCI DESCRIÇÃO DO PRODUTO']
    tabela_desejada['ITENS FINANCEIROS'] = tabela_desejada['ITENS FINANCEIROS'].str.split(" ", n=1).str[1]

    # Limpa o "itens" e "financeiros" das colunas
    apagar_itens = "ITENS"
    apagar_financeiros = "FINANCEIROS" 
    tabela_desejada.loc[tabela_desejada["DESCRIÇÃO DO PRODUTO"] == apagar_financeiros, 'DESCRIÇÃO DO PRODUTO'] = ' '
    tabela_desejada.loc[tabela_desejada["CCI"] == apagar_itens, 'CCI'] = ' '


    tabela_desejada[['coluna tarifa c/ impostos', 'coluna B. CÁLC ICMS']] = tabela_desejada['B. CÁLC ICMS'].str.split(" ", n=1, expand=True)

    
    # Substituir strings vazias e espaços por NaN
    tabela_desejada['TARIFA C/ IMPOSTOS'] = tabela_desejada['TARIFA C/ IMPOSTOS'].replace(['', ' '], np.nan)

    # Preencher NaN na coluna 'coluna tarifa c/ impostos' com valores da coluna 'B. CÁLC ICMS'
    teste = tabela_desejada['TARIFA C/ IMPOSTOS'] = tabela_desejada['TARIFA C/ IMPOSTOS'].fillna(tabela_desejada['coluna tarifa c/ impostos'])

    # Supondo que 'tabela_desejada' seja o seu DataFrame e as colunas já existam
#    teste = tabela_desejada['TARIFA C/ IMPOSTOS'] = tabela_desejada['TARIFA C/ IMPOSTOS'].fillna(tabela_desejada['coluna tarifa c/ impostos'])



    # Filtra os valores da coluna 'B. CÁLC ICMS' que possuem dois valores separados por espaço
#    valores_desejados = tabela_desejada['B. CÁLC ICMS'].astype(str).apply(lambda x: x.split() if len(x.split()) == 2 else None)



    # Filtra as linhas que possuem valores válidos
#   valores_desejados = valores_desejados[valores_desejados.notnull()]

    # Obtém o primeiro valor de cada célula
#    valores_desejados = valores_desejados.apply(lambda x: x[0])

    # Substitui os valores da coluna 'TARIFA C/ IMPOSTOS' pelos primeiros valores de 'B. CÁLC ICMS'
#    tabela_desejada[['TARIFA C/ IMPOSTOS']] = valores_desejados




    display(tabela_desejada)
else:
    print("Tabela desejada não encontrada.")

 
if tabela_desejada is not None:
    #tabela_desejada.to_csv("ddoeis.csv", index=False)

    # Salva somente as colunas desejadas 
    col_m = tabela_desejada.iloc[:, 12]
    col_n = tabela_desejada.iloc[:, 13]
    col_c = tabela_desejada.iloc[:, 2]
    col_o = tabela_desejada.iloc[:, 14]
    col_p = tabela_desejada.iloc[:, 15]
    col_q = tabela_desejada.iloc[:, 16]
    col_r = tabela_desejada.iloc[:, 17]
    col_e = tabela_desejada.iloc[:, 4]
    col_f = tabela_desejada.iloc[:, 5]
    col_g = tabela_desejada.iloc[:, 6]
    col_h = tabela_desejada.iloc[:, 7]
    col_i = tabela_desejada.iloc[:, 8]
    col_j = tabela_desejada.iloc[:, 9]
    col_k = tabela_desejada.iloc[:, 10]
    col_l = tabela_desejada.iloc[:, 11]
    col_s = tabela_desejada.iloc[:, 18]

    tabela_desejada = tabela_desejada.drop(1)
    resultado_final = pd.DataFrame({'CCI': col_m, 'DESCRIÇÃO DO PRODUTO': col_n, 'QTD': col_c,
                            'TARIFA APLICADA': col_o, 'VALOR FORNEC': col_p, 'TARIFA C/ IMPOSTOS': col_q,
                              'B. CÁLC ICMS': col_r, 'ALIQ ICMS%': col_e, 'VALOR ICMS': col_f, 'B.CÁLC PIS/COFINS': col_g,
                                'ALIQ PIS%': col_h, 'VALOR PIS': col_i, 'ALIQ COFINS%': col_j, 'VALOR COFINS': col_k, 'VALOR TOTAL': col_l,
                                  'ITENS FINANCEIROS': col_s})
    
    
    
    #resultado_final.to_csv("resultado.csv", index=False)

    display(teste)
    display(resultado_final)





# EXTRAINDO A SEGUNDA TABELA DE DEMOSTRATIVO DE VALORES

arquivo2 = tabula.read_pdf("edp.pdf", pages="all", multiple_tables=True)

# Quantidade de tabelas encontradas
print('Quantidade de tabelas na página: ', len(arquivo2))



tabela_dois = None
for coluna in arquivo2:
    if isinstance(coluna, pd.DataFrame) and not coluna.empty:
        # Verifica se a primeira linha da tabela contém o cabeçalho esperado
        if any("ALÍQUOTA" in str(cell) for cell in coluna.iloc[0]):
            tabela_dois = coluna
            
            break

if tabela_dois is not None:
    tabela_dois.columns = tabela_dois.iloc[0]

    tabela_dois[['ALÍQUOTA', 'VALOR (R$)']] = tabela_dois['ALÍQUOTA VALOR (R$)'].str.split(" ", n=1, expand=True)

    col_a = tabela_dois.iloc[:, 0]
    col_b = tabela_dois.iloc[:, 1]
    col_d = tabela_dois.iloc[:, 3]
    col_e = tabela_dois.iloc[:, 4]

    final_segunda_tabela = pd.DataFrame({'DESCRIÇÃO': col_a, 'BASE DE CÁLCULO': col_b, 'ALÍQUOTA': col_d, 'VALOR (R$)': col_e})

    final_segunda_tabela = final_segunda_tabela.drop(0)

    #final_segunda_tabela.to_csv("resultadoSegunda.csv", index=False)

    display(final_segunda_tabela)



# EXTRAINDO A TENSÃO CONTRATADA

arquivo3 = tabula.read_pdf("edp.pdf", pages="all", multiple_tables=True)

tabela_tres = None
for coluna in arquivo3:
    if isinstance(coluna, pd.DataFrame) and not coluna.empty:
        # Verifica se a primeira linha da tabela contém o cabeçalho esperado
        if any("Bandeira Tarifária Vigente" in str(cell) for cell in coluna.iloc[0]):
            tabela_tres = coluna
            #display(tabela_dois)
            break
    else:
        print("Erro ao encontrar a tabela")

if tabela_tres is not None:
  
    #Procurar o idx da tensão
    idx_tensao_contratada = tabela_tres[tabela_tres["Unnamed: 0"].str.contains("Tensão", na=False)].index[0]

    tabela_da_tensao = tabela_tres['TENSÃO CONTRATADA'] = tabela_tres.loc[idx_tensao_contratada + 1, 'Unnamed: 0']

    coluna_da_tensao = tabela_tres.iloc[:, 5]

    end_tensao = pd.DataFrame({'TENSÃO CONTRATADA': coluna_da_tensao})
    
    display(tabela_da_tensao)

    #coluna_da_tensao.to_csv("Finaliza.csv", index=False, header=['TENSÃO CONTRATADA'])


    col_m = tabela_desejada.iloc[:, 12]
    col_n = tabela_desejada.iloc[:, 13]
    col_c = tabela_desejada.iloc[:, 2]
    col_o = tabela_desejada.iloc[:, 14]
    col_p = tabela_desejada.iloc[:, 15]
    col_q = tabela_desejada.iloc[:, 16]
    col_r = tabela_desejada.iloc[:, 17]
    col_e = tabela_desejada.iloc[:, 4]
    col_f = tabela_desejada.iloc[:, 5]
    col_g = tabela_desejada.iloc[:, 6]
    col_h = tabela_desejada.iloc[:, 7]
    col_i = tabela_desejada.iloc[:, 8]
    col_j = tabela_desejada.iloc[:, 9]
    col_k = tabela_desejada.iloc[:, 10]
    col_l = tabela_desejada.iloc[:, 11]
    col_s = tabela_desejada.iloc[:, 18]

    col_a2 = tabela_dois.iloc[:, 0]
    col_b2 = tabela_dois.iloc[:, 1]
    col_d2 = tabela_dois.iloc[:, 3]
    col_e2 = tabela_dois.iloc[:, 4]

    col_a3 = tabela_tres.iloc[:, 5]
    geral = pd.DataFrame({'CCI': col_m, 'DESCRIÇÃO DO PRODUTO': col_n, 'QTD': col_c,
                            'TARIFA APLICADA': col_o, 'VALOR FORNEC': col_p, 'TARIFA C/ IMPOSTOS': col_q,
                              'B. CÁLC ICMS': col_r, 'ALIQ ICMS%': col_e, 'VALOR ICMS': col_f, 'B.CÁLC PIS/COFINS': col_g,
                                'ALIQ PIS%': col_h, 'VALOR PIS': col_i, 'ALIQ COFINS%': col_j, 'VALOR COFINS': col_k, 'VALOR TOTAL': col_l,
                                  'ITENS FINANCEIROS': col_s, 'DESCRIÇÃO': col_a2, 'BASE DE CÁLCULO': col_b2, 'ALÍQUOTA': col_d2, 'VALOR (R$)': col_e2, 'TENSÃO CONTRATADA': col_a3})
    geral = geral.drop(0)
    display(geral)
    geral.to_csv("FINZALIZAÇÃO.csv", index=False)
    print("O csv do boleto edp está pronto!")

