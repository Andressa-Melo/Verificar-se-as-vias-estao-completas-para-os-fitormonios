
import pandas as pd     #impotar biblioteca pandas
# entrada
arquivo = '/home/jessica/Downloads/5.Bacillus_thuringiensis_S_601.faa-kegg.txt'   
#arquivos de saida 
arquivo_saida = '/home/jessica/Área de Trabalho/Fitormonios/resultados fitormonios/fitormonios.xlsx'   

### Lista de fitormonios de interesse FIXO  ####
#metabolismo triptofano (00380)
#partir do triptofano
indolacetato_via1 = [['K01593', 'K22433'], ['K11868'], ['K01501']]
indolacetato_via2 = [['K11812','K11813'], ['K11868'], ['K01501']]
indolacetato_via3 = [['K01593', 'K22433'], ['K11818'], ['K11819'], ['K11820'], ['K11821'], ['K01237']]
indolacetato_via4 = [['K01593', 'K22433'], ['K11818'], ['K11819'], ['K11820'], ['K11821'], ['K01237'], ['K01721'], ['K20807'], ['K01426', 'K21801']]
indolacetato_via5 = [['K00466'], ['K01426', 'K21801']]
indolacetato_via6 = [['K03334', 'K14265', 'K00838', 'K16903'], ['K11816']]
indolacetato_via7 = [['K03334', 'K14265', 'K00838', 'K16903'], ['K04103'], ['K00128', 'K14085', 'K00149', 'K11817', 'K22417']]
indolacetato_via8 =[['K00128', 'K14085', 'K00149', 'K01593', 'K22433'], ['K11182', 'K00274'], ['K00128', 'K14085', 'K00149', 'K11817', 'K22417']]
indolacetato_via9 = [['K11812','K11813'],['K11818'], ['K11819'], ['K11820'], ['K11821'], ['K01501']]
indolacetato_via10 = [['K01593', 'K22433'], ['K11818'], ['K11819'], ['K11820'], ['K11821'], ['K01237'], ['K01501']]                  

#metabolismo alpha-Linolenic acid metabolism 00592
#partir do ácido alfa linolênico
jasmonato = [['K00454'], ['K01723'], ['K10525'], ['K05894'], ['K10526'], ['K00232'], ['K10527'], ['K00632', 'K07513'], ['K00232'], ['K10527'], ['K00632', 'K07513'], ['K00232'], ['K10527'], ['K00632', 'K07513']]

# Biossíntese de diterpenóides 00904
#partir da Geranylgeranyl-PP (GA1)
giberelina_via1 = [['K04120', 'K20657', 'K27636'], ['K04121', 'K20657', 'K27636'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04123', 'K12917'], ['K12917'], ['K12918'], ['K12919']]
giberelina_via2 = [['K04120', 'K20657', 'K27636'], ['K04121', 'K20657', 'K27636'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04123', 'K12917'], ['K04123'], ['K12918'], ['K12919']]
giberelina_via3 = [['K04120', 'K20657', 'K27636'], ['K04121', 'K20657', 'K27636'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04123', 'K12917'], ['K04123'], ['K05282'], ['K12918'], ['K12919']]
giberelina_via4 = [['K04120', 'K20657', 'K27636'], ['K04121', 'K20657', 'K27636'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04123', 'K12917'], ['K04123'], ['K05282'], ['K04124'], ['K12919']]
giberelina_via5 = [['K04120', 'K20657', 'K27636'], ['K04121', 'K20657', 'K27636'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04123', 'K12917'], ['K05282'], ['K04124']]
giberelina_via6 = [['K04120', 'K20657', 'K27636'], ['K04121', 'K20657', 'K27636'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04122', 'K21292'], ['K04123', 'K12917'], ['K05282'], ['K04124'], ['K24460'], ['K04124']]

# Biossíntese de carotenóides 00906
#partir do Terpenoid backbone biosynthesis (inicio do metabolismo)
strigol_via1 = [['K02291', 'K17841'], ['K02293'], ['K15744'], ['K00514'], ['K09835'], ['K06443', 'K22502', 'K17841', 'K14605', 'K14606'], ['K06443', 'K22502', 'K17841', 'K14605', 'K14606'], ['K17911'], ['K17912'], ['K17913']]
strigol_via2 = [['K02291', 'K17841'], ['K10027', 'K15745', 'K02293'], ['K10027', 'K15745', 'K02293', 'K00514'], ['K06443', 'K22502', 'K17841', 'K14605', 'K14606'], ['K06443', 'K22502', 'K17841', 'K14605', 'K14606'], ['K17911'], ['K17912'], ['K17913']]

# Biossíntese de carotenóides 00906
#partir do Terpenoid backbone biosynthesis (inicio do metabolismo)
abscisico_via1 = [['K02291', 'K17841'], ['K10027', 'K15745', 'K02293'], ['K10027', 'K15745', 'K02293', 'K00514'], ['K06443', 'K22502', 'K17841', 'K14605', 'K14606'], ['K02294', 'K15746', 'K22492', 'K23037', 'K15747'], ['K15747', 'K02294', 'K15746', 'K22492', 'K23037'], ['K09838'], ['K09840'], ['K09841'], ['K09842']]
abscisico_via2 = [['K02291', 'K17841'], ['K10027', 'K15745', 'K02293'], ['K10027', 'K15745', 'K02293', 'K00514'], ['K06443', 'K22502', 'K17841', 'K14605', 'K14606'], ['K02294', 'K15746', 'K22492', 'K23037', 'K15747'], ['K15747', 'K02294', 'K15746', 'K22492', 'K23037'], ['K09838'], ['K14594'], ['K09840'], ['K09841'], ['K09842']]

# Metabolismo da cisteína e metionina 00270
# partir do metabolismo sulfato
etileno = [['K00544', 'K00547', 'K00548', 'K24042', 'K00549'], ['K00789'], ['K20772', 'K01762'], ['K05933']]

# Chloroalkane and chloroalkene degradation- partir do tetracloroeteno (00625)
etilenocloro = [['K21647', 'K21648']]

# Metablismo Biossíntese de peptídeos não ribossômicos do grupo sideróforo (01053)
salicilato = [['K01851', 'K02361', 'K02552', 'K04781'], ['K04782', 'K04781']]

#Naphthalene degradation (00626) partir do naftaleno
salicilatonafitaleno = [['K14579', 'K14580', 'K14578', 'K14581'], ['K14582'], ['K14583'], ['K14584'],['K14585'], ['K00152']]

# Dioxin degradation (00621) partir do dibenzofurano
salicilatodioxin = [['K14599', 'K14600', 'K22715', 'K22716'], ['K15749'], ['K22717']]


### FUNÇÃO QUE VERIFICA AS ETAPAS DAS ENZIMAS ####
def fitormonios (valores, conteudo):
    resultados = []
    for i, valores in enumerate(valores, start=1):
        etapa = i
        enzima_encontrada = False
        for valor in valores:
            encontrado = any(valor in linha for linha in conteudo)
            if encontrado:
                resultados.append([valor, 'Existe', f'Etapa {etapa}'])
                enzima_encontrada = True   
            else:
                resultados.append([valor, 'N/E', f'Etapa {etapa}'])
        if enzima_encontrada:
            resultados.append(['', '', f'Etapa {etapa} Completa'])
        else:
            resultados.append(['', '', f'Etapa {etapa} Incompleta'])
    return resultados

### Ler o arquivo e obter o conteúdo ####
with open(arquivo, 'r') as file:
    conteudo = file.readlines()  # Lê todas as linhas do arquivo (readlines) (NÃO USEI O SEPARADOR SPLIT ('\t') e ele conseguiu fazer a busca, se surgir algum bug nesse sentido, adicionar linha comentada)
    #arquivo = [linha.strip().split('\t') for linha in conteudo]

### Chamar a função para verificar enzimas na via ###
resultados_indolacetato_via1 = fitormonios(indolacetato_via1, conteudo)
resultados_indolacetato_via2 = fitormonios(indolacetato_via2, conteudo)
resultados_indolacetato_via3 = fitormonios(indolacetato_via3, conteudo)
resultados_indolacetato_via4 = fitormonios(indolacetato_via4, conteudo)
resultados_indolacetato_via5 = fitormonios(indolacetato_via5, conteudo)
resultados_indolacetato_via6 = fitormonios(indolacetato_via6, conteudo)
resultados_indolacetato_via7 = fitormonios(indolacetato_via7, conteudo)
resultados_indolacetato_via8 = fitormonios(indolacetato_via8, conteudo)
resultados_indolacetato_via9 = fitormonios(indolacetato_via9, conteudo)
resultados_indolacetato_via10 = fitormonios(indolacetato_via10, conteudo)

resultados_jasmonato = fitormonios(jasmonato, conteudo)

resultados_giberelina_via1 = fitormonios(giberelina_via1, conteudo)
resultados_giberelina_via2 = fitormonios(giberelina_via2, conteudo)
resultados_giberelina_via3 = fitormonios(giberelina_via3, conteudo)
resultados_giberelina_via4 = fitormonios(giberelina_via4, conteudo)
resultados_giberelina_via5 = fitormonios(giberelina_via5, conteudo)
resultados_giberelina_via6 = fitormonios(giberelina_via6, conteudo)

resultados_strigol_via1 = fitormonios(strigol_via1, conteudo)
resultados_strigol_via2 = fitormonios(strigol_via2, conteudo)

resultados_abscisico_via1 = fitormonios(abscisico_via1, conteudo)
resultados_abscisico_via2 = fitormonios(abscisico_via2, conteudo)

resultados_etileno = fitormonios(etileno, conteudo)

resultados_etilenocloro = fitormonios(etilenocloro, conteudo)

resultados_salicilato = fitormonios(salicilato, conteudo)

resultados_salicilatonafitaleno = fitormonios(salicilatonafitaleno, conteudo)

resultados_salicilatodioxin = fitormonios(salicilatodioxin, conteudo)

###  Criar DataFrames para cada conjunto de resultados

df_indolacetato_via1 = pd.DataFrame(resultados_indolacetato_via1, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via2 = pd.DataFrame(resultados_indolacetato_via2, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via3 = pd.DataFrame(resultados_indolacetato_via3, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via4 = pd.DataFrame(resultados_indolacetato_via4, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via5 = pd.DataFrame(resultados_indolacetato_via5, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via6 = pd.DataFrame(resultados_indolacetato_via6, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via7 = pd.DataFrame(resultados_indolacetato_via7, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via8 = pd.DataFrame(resultados_indolacetato_via8, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via9 = pd.DataFrame(resultados_indolacetato_via9, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_indolacetato_via10 = pd.DataFrame(resultados_indolacetato_via10, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_jasmonato = pd.DataFrame(resultados_jasmonato, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_giberelina_via1 = pd.DataFrame(resultados_giberelina_via1, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_giberelina_via2 = pd.DataFrame(resultados_giberelina_via2, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_giberelina_via3 = pd.DataFrame(resultados_giberelina_via3, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_giberelina_via4 = pd.DataFrame(resultados_giberelina_via4, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_giberelina_via5 = pd.DataFrame(resultados_giberelina_via5, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_giberelina_via6 = pd.DataFrame(resultados_giberelina_via6, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_strigol_via1 = pd.DataFrame(resultados_strigol_via1, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_strigol_via2 = pd.DataFrame(resultados_strigol_via2, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_abscisico_via1 = pd.DataFrame(resultados_abscisico_via1, columns=['Enzima', 'Status', 'Etapas da via metabólica'])
df_abscisico_via2 = pd.DataFrame(resultados_abscisico_via2, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_etileno = pd.DataFrame(resultados_etileno, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_etilenocloro = pd.DataFrame(resultados_etilenocloro, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_salicilato = pd.DataFrame(resultados_salicilato, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_salicilatonafitaleno = pd.DataFrame(resultados_salicilatonafitaleno, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_salicilatodioxin = pd.DataFrame(resultados_salicilatodioxin, columns=['Enzima', 'Status', 'Etapas da via metabólica'])

df_resultado_total = pd.DataFrame(columns=['Resultado Geral'])  # DataFrame geral para resultados

### Função para verificar se a via metabólica está completa ###
def verificar_via(df, total_etapas):
    etapas_completas = set()  
    for etapa in df[df['Status'] == 'Existe']['Etapas da via metabólica']:
        etapa_numero = int(etapa.split(' ')[1])  # Extrai o número 0 da etapa
        etapas_completas.add(etapa_numero)
    # Verifica se todas as etapas esperadas foram completadas
    return len(etapas_completas) == total_etapas

### Contar total de etapas para cada grupo ###
total_etapas_indolacetato_via1 = len(indolacetato_via1) 
total_etapas_indolacetato_via2 = len(indolacetato_via2)
total_etapas_indolacetato_via3 = len(indolacetato_via3)
total_etapas_indolacetato_via4 = len(indolacetato_via4)
total_etapas_indolacetato_via5 = len(indolacetato_via5)
total_etapas_indolacetato_via6 = len(indolacetato_via6)
total_etapas_indolacetato_via7 = len(indolacetato_via7)
total_etapas_indolacetato_via8 = len(indolacetato_via8)
total_etapas_indolacetato_via9 = len(indolacetato_via9)
total_etapas_indolacetato_via10 = len(indolacetato_via10)

total_etapas_jasmonato = len(jasmonato)

total_etapas_giberelina_via1 = len(giberelina_via1)
total_etapas_giberelina_via2 = len(giberelina_via2)
total_etapas_giberelina_via3 = len(giberelina_via3)
total_etapas_giberelina_via4 = len(giberelina_via4)
total_etapas_giberelina_via5 = len(giberelina_via5)
total_etapas_giberelina_via6 = len(giberelina_via6)

total_etapas_strigol_via1 = len(strigol_via1)
total_etapas_strigol_via2 = len(strigol_via2)

total_etapas_abscisico_via1 = len(abscisico_via1)
total_etapas_abscisico_via2 = len(abscisico_via2)

total_etapas_etileno = len(etileno)

total_etapas_etilenocloro = len(etilenocloro)

total_etapas_salicilato = len(salicilato)

total_etapas_salicilatonafitaleno = len(salicilatonafitaleno)

total_etapas_salicilatodioxin = len(salicilatodioxin)

### Verificar se a via é completa ###
via_completa_indolacetato_via1 = verificar_via(df_indolacetato_via1, total_etapas_indolacetato_via1)
via_completa_indolacetato_via2 = verificar_via(df_indolacetato_via2, total_etapas_indolacetato_via2)
via_completa_indolacetato_via3 = verificar_via(df_indolacetato_via3, total_etapas_indolacetato_via3)
via_completa_indolacetato_via4 = verificar_via(df_indolacetato_via4, total_etapas_indolacetato_via4)
via_completa_indolacetato_via5 = verificar_via(df_indolacetato_via5, total_etapas_indolacetato_via5)
via_completa_indolacetato_via6 = verificar_via(df_indolacetato_via6, total_etapas_indolacetato_via6)
via_completa_indolacetato_via7 = verificar_via(df_indolacetato_via7, total_etapas_indolacetato_via7)
via_completa_indolacetato_via8 = verificar_via(df_indolacetato_via8, total_etapas_indolacetato_via8)
via_completa_indolacetato_via9 = verificar_via(df_indolacetato_via9, total_etapas_indolacetato_via9)
via_completa_indolacetato_via10 = verificar_via(df_indolacetato_via10, total_etapas_indolacetato_via10)

via_completa_jasmonato = verificar_via(df_jasmonato, total_etapas_jasmonato)

via_completa_giberelina_via1 = verificar_via(df_giberelina_via1, total_etapas_giberelina_via1)
via_completa_giberelina_via2 = verificar_via(df_giberelina_via2, total_etapas_giberelina_via2)
via_completa_giberelina_via3 = verificar_via(df_giberelina_via3, total_etapas_giberelina_via3)
via_completa_giberelina_via4 = verificar_via(df_giberelina_via4, total_etapas_giberelina_via4)
via_completa_giberelina_via5 = verificar_via(df_giberelina_via5, total_etapas_giberelina_via5)
via_completa_giberelina_via6 = verificar_via(df_giberelina_via6, total_etapas_giberelina_via6)

via_completa_strigol_via1 = verificar_via(df_strigol_via1, total_etapas_strigol_via1)
via_completa_strigol_via2 = verificar_via(df_strigol_via2, total_etapas_strigol_via2)

via_completa_abscísico_via1 = verificar_via(df_abscisico_via1, total_etapas_abscisico_via1)
via_completa_abscísico_via2 = verificar_via(df_abscisico_via2, total_etapas_abscisico_via2)

via_completa_etileno = verificar_via(df_etileno, total_etapas_etileno)

via_completa_etilenocloro= verificar_via(df_etilenocloro, total_etapas_etilenocloro)

via_completa_salicilato = verificar_via(df_salicilato, total_etapas_salicilato)

via_completa_salicilatonafitaleno = verificar_via(df_salicilatonafitaleno, total_etapas_salicilatonafitaleno)

via_completa_salicilatodioxin = verificar_via(df_salicilatodioxin, total_etapas_salicilatodioxin)

### função para adicionar o resultado geral a partir dos resultados dos status da via
def adicionar_status(df_resultado, nome_via, status_via):
    nova_linha = pd.DataFrame({'Resultado Geral': [f'{nome_via}: {status_via}']})
    df_resultado = pd.concat([df_resultado, nova_linha], ignore_index=True)
    return df_resultado

status_indolacetato_via1 = 'Via Completa' if via_completa_indolacetato_via1 else 'Via Incompleta'
status_indolacetato_via2 = 'Via Completa' if via_completa_indolacetato_via2 else 'Via Incompleta'
status_indolacetato_via3 = 'Via Completa' if via_completa_indolacetato_via3 else 'Via Incompleta'
status_indolacetato_via4 = 'Via Completa' if via_completa_indolacetato_via4 else 'Via Incompleta'
status_indolacetato_via5 = 'Via Completa' if via_completa_indolacetato_via5 else 'Via Incompleta'
status_indolacetato_via6 = 'Via Completa' if via_completa_indolacetato_via6 else 'Via Incompleta'
status_indolacetato_via7 = 'Via Completa' if via_completa_indolacetato_via7 else 'Via Incompleta'
status_indolacetato_via8 = 'Via Completa' if via_completa_indolacetato_via8 else 'Via Incompleta'
status_indolacetato_via9 = 'Via Completa' if via_completa_indolacetato_via9 else 'Via Incompleta'
status_indolacetato_via10 = 'Via Completa' if via_completa_indolacetato_via10 else 'Via Incompleta'

status_jasmonato = 'Via Completa' if via_completa_jasmonato else 'Via Incompleta'

status_giberelina_via1 = 'Via Completa' if via_completa_giberelina_via1 else 'Via Incompleta'
status_giberelina_via2 = 'Via Completa' if via_completa_giberelina_via2 else 'Via Incompleta'
status_giberelina_via3 = 'Via Completa' if via_completa_giberelina_via3 else 'Via Incompleta'
status_giberelina_via4 = 'Via Completa' if via_completa_giberelina_via4 else 'Via Incompleta'
status_giberelina_via5 = 'Via Completa' if via_completa_giberelina_via5 else 'Via Incompleta'
status_giberelina_via6 = 'Via Completa' if via_completa_giberelina_via6 else 'Via Incompleta'

status_strigol_via1 = 'Via Completa' if via_completa_strigol_via1 else 'Via Incompleta'
status_strigol_via2 = 'Via Completa' if via_completa_strigol_via2 else 'Via Incompleta'

status_abscisico_via1 = 'Via Completa' if via_completa_abscísico_via1 else 'Via Incompleta'
status_abscisico_via2 = 'Via Completa' if via_completa_abscísico_via2 else 'Via Incompleta'

status_etileno  = 'Via Completa' if via_completa_etileno else 'Via Incompleta'

status_etilenocloro = 'Via Completa' if via_completa_etilenocloro else 'Via Incompleta'

status_salicilato  = 'Via Completa' if via_completa_salicilato  else 'Via Incompleta'

status_salicilatonafitaleno = 'Via Completa' if via_completa_salicilatonafitaleno else 'Via Incompleta'

status_salicilatodioxin = 'Via Completa' if via_completa_salicilatodioxin else 'Via Incompleta'

# Adicionar o status das vias ao DataFrame 'Resultado Geral'
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 1 (triptofano)', status_indolacetato_via1)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 2 (triptofano)', status_indolacetato_via2)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 3 (triptofano)', status_indolacetato_via3)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 4 (triptofano)', status_indolacetato_via4)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 5 (triptofano)', status_indolacetato_via5)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 6 (triptofano)', status_indolacetato_via6)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 7 (triptofano)', status_indolacetato_via7)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 8 (triptofano)', status_indolacetato_via8)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 9 (triptofano)', status_indolacetato_via9)
df_resultado_total = adicionar_status(df_resultado_total, 'Indolacetato 10 (triptofano)', status_indolacetato_via10)

df_resultado_total = adicionar_status(df_resultado_total, 'Jasmonato (ácido linolênico)', status_jasmonato)

df_resultado_total = adicionar_status(df_resultado_total, 'Giberelina 1 (Bios. diterpenóides)', status_giberelina_via1)
df_resultado_total = adicionar_status(df_resultado_total, 'Giberelina 2 (Bios. diterpenóides)', status_giberelina_via2)
df_resultado_total = adicionar_status(df_resultado_total, 'Giberelina 3 (Bios. diterpenóides)', status_giberelina_via3)
df_resultado_total = adicionar_status(df_resultado_total, 'Giberelina 4 (Bios. diterpenóides)', status_giberelina_via4)
df_resultado_total = adicionar_status(df_resultado_total, 'Giberelina 5 (Bios. diterpenóides)', status_giberelina_via5)
df_resultado_total = adicionar_status(df_resultado_total, 'Giberelina 6 (Bios. diterpenóides)', status_giberelina_via6)

df_resultado_total = adicionar_status(df_resultado_total, 'Strigol 1 (Bios. carotenóides)', status_strigol_via1)
df_resultado_total = adicionar_status(df_resultado_total, 'Strigol 2 (Bios. carotenóides)', status_strigol_via2)

df_resultado_total = adicionar_status(df_resultado_total, 'Abscísico 1 (Bios. carotenóides)', status_abscisico_via1)
df_resultado_total = adicionar_status(df_resultado_total, 'Abscísico 2 (Bios. carotenóides)', status_abscisico_via2)

df_resultado_total = adicionar_status(df_resultado_total, 'Etileno (cisteína e metionina)', status_etileno)

df_resultado_total = adicionar_status(df_resultado_total, 'Etileno (cloroalcano)', status_etilenocloro)

df_resultado_total = adicionar_status(df_resultado_total, 'Salicilato (bios. peptídeos não ribossómico)', status_salicilato)

df_resultado_total = adicionar_status(df_resultado_total, 'Salicilato (naftaleno)', status_salicilatonafitaleno)

df_resultado_total = adicionar_status(df_resultado_total, 'Salicilato (degra. de dioxina)', status_salicilatodioxin)

# Função para combinar DataFrames com cabeçalhos numerados
def combinar_dataframes_com_numeracao(dfs, prefixo_nome):
    df_combined = pd.DataFrame()
    for i, df in enumerate(dfs, start=1):
        # Adiciona o prefixo e a numeração ao cabeçalho das colunas
        df_temp = df.copy()
        df_temp.columns = [f'{col} {i}' for col in df.columns]
        
        # Adiciona os DataFrames ao combinado
        df_combined = pd.concat([df_combined, df_temp], axis=1)
        
        # Adiciona uma coluna em branco para separar
        if i < len(dfs):
            df_blank = pd.DataFrame('', index=df_combined.index, columns=[''] * len(df.columns))
            df_combined = pd.concat([df_combined, df_blank], axis=1)
    return df_combined

# Listas de DataFrames para cada categoria
dataframeindolacetato= [df_indolacetato_via1, df_indolacetato_via2, df_indolacetato_via3,
                        df_indolacetato_via4, df_indolacetato_via5, df_indolacetato_via6,
                        df_indolacetato_via7, df_indolacetato_via8, df_indolacetato_via9,
                        df_indolacetato_via10]

dataframegiberelina = [df_giberelina_via1, df_giberelina_via2, df_giberelina_via3,
                    df_giberelina_via4, df_giberelina_via5, df_giberelina_via6]

dataframestrigol = [df_strigol_via1, df_strigol_via2]

dataframeabscisico = [df_abscisico_via1, df_abscisico_via2]

# Crie um arquivo Excel com múltiplas abas
with pd.ExcelWriter(arquivo_saida, engine='openpyxl') as writer:
    # Combinar e salvar cada grupo de DataFrames
    df_indolacetato = combinar_dataframes_com_numeracao(dataframeindolacetato, 'Indolacetato (triptofano)')
    df_giberelina = combinar_dataframes_com_numeracao(dataframegiberelina, 'Giberelina (Bios. diterpenóides)')
    df_strigol = combinar_dataframes_com_numeracao(dataframestrigol, 'Strigol (Bios. carotenóides)')
    df_abscisico = combinar_dataframes_com_numeracao(dataframeabscisico, 'Abscísico (Bios. carotenóides)')

    # Salve cada DataFrame em uma aba separada
    df_indolacetato.to_excel(writer, sheet_name='Indolacetato (triptofano)', index=False)
    df_giberelina.to_excel(writer, sheet_name='Giberelina (Bios. diterpenóides)', index=False)
    df_strigol.to_excel(writer, sheet_name='Strigol (Bios. carotenóides)', index=False)
    df_abscisico.to_excel(writer, sheet_name='Abscísico (Bios. carotenóides)', index=False)

    df_jasmonato.to_excel(writer, sheet_name='Jasmonato (ácido linolênico)', index=False)

    df_etileno.to_excel(writer, sheet_name='Etileno (cisteína e metionina)', index=False)

    df_etilenocloro.to_excel(writer, sheet_name='Etileno (cloroalcano)', index=False)

    df_salicilato.to_excel(writer, sheet_name='Salicilato (bios. peptídeos não ribossómico)', index=False)

    df_salicilatonafitaleno.to_excel(writer, sheet_name='Salicilato (naftaleno)', index=False)

    df_salicilatodioxin.to_excel(writer, sheet_name='Salicilato (degra. de dioxina)', index=False)

    df_resultado_total.to_excel(writer, sheet_name='Resultado Geral', index=False)    

print(f'Resultados foram gravados em {arquivo_saida}')

