import tabula
import pandas as pd
from IPython.display import display 
import numpy as np



arquivo_enel = tabula.read_pdf("ENELSP.pdf", pages="all", multiple_tables=True)


print('Quantidade de tabelas na página: ', len(arquivo_enel))


tabela_puxada = None
for tabela in arquivo_enel:
    if isinstance(tabela, pd.DataFrame) and not tabela.empty:
        # Verifica se a primeira linha da tabela contém o cabeçalho esperado
        if any("Itens de" in str(cell) for cell in tabela.iloc[0]):
            tabela_puxada = tabela
            break


if tabela_puxada is not None:
    tabela_puxada = tabela_puxada.iloc[:14]
    tabela_puxada = tabela_puxada.iloc[:, :7]
    tabela_puxada[['QUANT. (kWh)', 'Preço unit (R$) com tributos']] = tabela_puxada['TIPO DE Quant. Preço unit (R$)'].str.split(" ", n=1, expand=True)
    tabela_puxada[['Valor (R$)', 'PIS/COFINS']] = tabela_puxada['PIS/'].str.split(" ", n=1, expand=True)
    tabela_puxada[['ICMS', 'Tarifa unit (R$)']] = tabela_puxada['Tarifa'].str.split(" ", n=1, expand=True)
    display(tabela_puxada)

    a_segundo = tabela_puxada.iloc[:, 0]
    b_segundo = tabela_puxada.iloc[:, 1]
    c_segundo = tabela_puxada.iloc[:, 7]
    d_segundo = tabela_puxada.iloc[:, 8]
    e_segundo = tabela_puxada.iloc[:, 9]
    f_segundo = tabela_puxada.iloc[:, 10]

    g_segundo = tabela_puxada.iloc[:, 4]
    h_segundo = tabela_puxada.iloc[:, 5]
    i_segundo = tabela_puxada.iloc[:, 5]
    i_segundo = tabela_puxada.iloc[:, 11]
    j_segundo = tabela_puxada.iloc[:, 12]

    
    puxando_dados_segundo_arquivo = pd.DataFrame({'Itens de Fatuda': a_segundo, 'Unid.': b_segundo, 'Quant. (kWh)': c_segundo, 'Preço unit (R$) com tributos': d_segundo,
                                                'Valor(R$)': e_segundo, 'PIS/COFINS': f_segundo, 'Base ICMS (R$)': g_segundo, 
                                                  'Alíquota ICMS': h_segundo, 'ICMS': i_segundo, 
                                                  'Tarifa unit (R$)': j_segundo})
    puxando_dados_segundo_arquivo.to_csv("Segundo arquivo.csv", index=False)
    print("O csv do boleto enel está pronto!")

else:
    print("Erro")