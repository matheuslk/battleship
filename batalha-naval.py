from asyncio.windows_events import NULL
import os
matriz_valores = [0] * 20
# MATRIZ COM OS CARACTERES DAS LINHAS QUE SERÃO EXIBIDOS NA VERTICAL AO LADO DA MATRIZ PRINCIPAL
linhas_matriz = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
# MATRIZ COM OS CARACTERES DAS LINHAS QUE SERÃO EXIBIDOS NA VERTICAL AO LADO DA MATRIZ PRINCIPAL
colunas_matriz = ['0', '1', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
# PREENCHIMENTO DA MATRIZ PRINCIPAL COM ▮ INDICANDO QUE A POSIÇÃO ESTÁ VAZIA, A VARIÁVEL MATRIZ VALORES CONTERÁ ▮ CASO ESTIVER VAZIA, 0 CASO SEJA PARTE DE UMA FRAGATA, 1 CASO SEJA PARTE DE UM CRUZADOR E 2 CASO SEJA PARTE DE UM PORTA AVIÃO
for linha in range(len(matriz_valores)):
  matriz_valores[linha] = ['▮'] * 20
# OS VALORES DA LINHA 14 ATÉ A LINHA 16 INDICAM A PARTE DE UMA EMBARCAÇÃO
PORTA_AVIAO = '2'
CRUZADOR = '1'
FRAGATA = '0'
# QUANTIDADE DE PORTA AVIÕES QUE PODERÃO SER CADASTRADOS NO JOGO
quantidade_porta_aviao = 3
# QUANTIDADE DE PARTES QUE UM PORTA AVIÃO TERÁ
tamanho_porta_aviao = 4
# VARIAVEL QUE GUARDARÁ TODAS AS POSIÇÕES (LINHA E COLUNA) DOS PORTA AVIÕES CADASTRADOS, SERÁ ÚTIL NA HORA DE CALCULAR OS PONTOS DO USUÁRIO POIS CADA VEZ QUE UM ATAQUE ACONTECER, CONSEGUIREMOS SABER O QUE FOI ACERTADO
posicoes_porta_aviao = []

# QUANTIDADE DE CRUZADORES QUE PODERÃO SER CADASTRADOS NO JOGO
quantidade_cruzador = 4
# QUANTIDADE DE PARTES QUE UM CRUZADOR TERÁ
tamanho_cruzador = 3
# VARIAVEL QUE GUARDARÁ TODAS AS POSIÇÕES (LINHA E COLUNA) DOS CRUZADORES CADASTRADOS, SERÁ ÚTIL NA HORA DE CALCULAR OS PONTOS DO USUÁRIO POIS CADA VEZ QUE UM ATAQUE ACONTECER, CONSEGUIREMOS SABER O QUE FOI ACERTADO
posicoes_cruzador = []

# QUANTIDADE DE FRAGATAS QUE PODERÃO SER CADASTRADAS NO JOGO
quantidade_fragata = 5
# QUANTIDADE DE PARTES QUE UMA FRAGATA TERÁ
tamanho_fragata = 2
# VARIAVEL QUE GUARDARÁ TODAS AS POSIÇÕES (LINHA E COLUNA) DAS FRAGATAS CADASTRADAS, SERÁ ÚTIL NA HORA DE CALCULAR OS PONTOS DO USUÁRIO POIS CADA VEZ QUE UM ATAQUE ACONTECER, CONSEGUIREMOS SABER O QUE FOI ACERTADO
posicoes_fragata = []
# VARIÁVEL QUE INDICA A QUANTIDADE DE PONTOS RECEBIDOS AO NAUFRAGAR, RESPECTIVAMENTE, UMA FRAGATA, UM CRUZADOR E UM PORTA AVIÃO
pontuacoes = [10, 20, 30]

# FUNÇAO QUE MONTARÁ UMA MATRIZ TRIDIMENSIONAL QUE SERÁ UTILIZADA PARA GUARDAR TODAS AS LINHAS E COLUNAS DE TODAS AS EMBARCAÇOES DO JOGO

# ESSA FUNÇAO SERÁ CHAMADA NAS LINHAS 66, 68 E 70, E EM CADA CHAMADA É POSSÍVEL VERIFICAR A PASSAGEM DE UM PARÂMETRO QUE INDICA UM TIPO DE EMBARCAÇAO

# NA PRÁTICA, NA LINHA 68 A FUNÇÃO É CHAMADA COM O PARÂMETRO INDEX_TIPO_EMBARCAÇAO VALENDO 0, E VALE LEMBRAR QUE O NÚMERO 0 CORRESPONDE A UMA FRAGATA, O 1 CORRESPONDE A UM CRUZADOR E O DOIS A UM PORTA AVIÃO

# VOLTANDO AO EXEMPLO, O RESULTADO DESSA FUNÇAO RETORNARÁ A SEGUINTE MATRIZ:
[[[0, 0], [0, 0]], [[0, 0], [0, 0]], [
    [0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]]
# ATÉ AQUI VAI ESTAR MUITO CONFUSO PROVAVELMENTE, MAS A IDEIA É A SEGUINTE:
# ESSA MATRIZ TRIDIMENSIONAL TERÁ 5 MATRIZES DENTRO DELA, QUE CORRESPONDEM A TODAS AS 5 FRAGATAS CONTIDAS NO JOGO, E CADA UMA DESSAS 5 MATRIZES CONTERÃO DOIS VETORES COM DOIS ESPAÇOS, QUE CORRESPONDEM RESPECTIVAMENTE A UMA LINHA E UMA COLUNA DA FRAGATA, FAZER ESSE MAPEAMENTO DE POSIÇOES É O QUE NOS PERMITE SABER QUANDO UMA EMBARCAÇAO FOI NAUFRAGADA, ISSO SERÁ EXPLICADO EM OUTRA FUNÇAO
# OS VALORES INICIAÇÃO COMO 0 POIS A MATRIZ ESTÁ SENDO CRIADA E O USUÁRIO AINDA NÃO COMEÇOU A CADASTRAR SUAS EMBARCACOES, A MEDIDA QUE ELE FOR CADASTRANDO AS POSICOES SERAO POPULADAS


def calcular_posicoes_embarcacao(tipo_embarcacao):
  quantidade_embarcacao = 0
  tamanho_embarcacao = 0
  if(tipo_embarcacao == 0):
    quantidade_embarcacao = quantidade_fragata
    tamanho_embarcacao = tamanho_fragata
  elif(tipo_embarcacao == 1):
    quantidade_embarcacao = quantidade_cruzador
    tamanho_embarcacao = tamanho_cruzador
  else:
    quantidade_embarcacao = quantidade_porta_aviao
    tamanho_embarcacao = tamanho_porta_aviao
  posicoes_embarcacao = [0] * quantidade_embarcacao
  for index_posicoes_embarcacao in range(quantidade_embarcacao):
    posicoes_embarcacao[index_posicoes_embarcacao] = [
        0] * tamanho_embarcacao
    for index_posicao in range(len(posicoes_embarcacao[index_posicoes_embarcacao])):
      posicoes_embarcacao[index_posicoes_embarcacao][index_posicao] = [0, 0]
  return posicoes_embarcacao


# AQUI É CHAMADA A FUNÇAO DA LINHA 50 PARA FAZER O MAPEAMENTO DAS POSICOES DAS EMBARCACOES E ARMAZENAR NAS VARIAVEIS DE POSICAO QUE SERÃO UTILIZADAS POR NÓS: posicoes_fragata, posicoes_cruzador e posicoes_porta_aviao
for index_tipo_embarcacao in range(3):
  if(index_tipo_embarcacao == 0):
    posicoes_fragata = calcular_posicoes_embarcacao(index_tipo_embarcacao)
  elif index_tipo_embarcacao == 1:
    posicoes_cruzador = calcular_posicoes_embarcacao(index_tipo_embarcacao)
  else:
    posicoes_porta_aviao = calcular_posicoes_embarcacao(index_tipo_embarcacao)

# FUNÇAO RESPONSÁVEL POR ATUALIZAR OS VALORES DAS POSICOES DAS EMBARCACOES (LINHA E COLUNA) QUANDO UM USUÁRIO DECIDIR CADASTRAR UMA EMBARCAÇAO, POR EXEMPLO: QUANDO ESSA FUNÇAO FOR CHAMADA, ELA RECEBERÁ POR PARÂMETRO A LINHA E A COLUNA ONDE A EMBARCAÇAO SERÁ CADASTRADA, O TIPO DA EMBARCACAO (0=FRAGATA, 1=CRUZADOR, 2=PORTA AVIAO) E ENTÃO IRÁ FAZER A ATUALIZAÇÃO DAS POSICOES DAS EMBARCACOES, POR EXEMPLO:
# DIGAMOS QUE O USUÁRIO IRÁ CADASTRAR O PRIMEIRO PORTA AVIÃO DO JOGO NA LINHA A COLUNA 10, O RETORNO DESSA FUNÇAO SERA O SEGUINTE:
[[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [0, 0], [0, 0], [0, 0]], [
    [0, 0], [0, 0], [0, 0], [0, 0]]]


def atualizar_posicoes_embarcacao(linha, coluna, tipo_embarcacao, index_embarcacao):
  todas_posicoes = [posicoes_porta_aviao, posicoes_cruzador, posicoes_fragata]
  for index_posicao in range(len(todas_posicoes[tipo_embarcacao][index_embarcacao])):
    todas_posicoes[tipo_embarcacao][index_embarcacao][index_posicao] = [
        linha, coluna+index_posicao]

# FUNÇAO RESPONSAVEL POR FAZER O DESENHO DO TABULEIRO, LEMBRANDO QUE HAVERÃO DUAS MATRIZES DE TABULEIRO, A PRIMEIRA REFERENTE AO CADASTRO DAS EMBARCAÇOES (matriz_valores), ONDE SERÁ PREENCHIDA PELO USUÁRIO, E A SEGUNDA MATRIZ SERÁ PREENCHIDA PELO USUÁRIO NA HORA DO ATAQUE


def desenhar_tabuleiro(matriz):
  for linha in range(len(matriz)):
    if(linha == 0):
      for index_numero_coluna in range(20):
        if(index_numero_coluna == 0):
          print(f'  {index_numero_coluna}', end='')
        elif(index_numero_coluna == 19):
          print(f' {index_numero_coluna}')
        elif(index_numero_coluna > 0 and index_numero_coluna < 10):
          print(f'  {index_numero_coluna}', end='')
        elif(index_numero_coluna == 10):
          print(f'  {index_numero_coluna}', end='')
        elif(index_numero_coluna > 10):
          print(f' {index_numero_coluna}', end='')
    for coluna in range(20):
      if(coluna == 0):
        print(
            f'{linhas_matriz[linha]} {matriz[linha][coluna]}  ', end='')
      elif (coluna == 19):
        print(f'{matriz[linha][coluna]}')
      else:
        print(f'{matriz[linha][coluna]}  ', end='')

# CADASTRO DE EMBARCAÇÕES


os.system('cls||clear')
# BLOCO DE CÓDIGO QUE VAI PEDIR PARA O USUÁRIO CADASTRAR SUAS EMBARCAÇÕES E CONFORME ELE FOR SELECIONANDO A LINHA E A COLUNA DELAS, A FUNÇAO atualizar_posicoes_embarcacao SERÁ CHAMADA NA LINHA 170 PARA ATUALIZAR AS POSICOES DAS EMBARCACOES, ASSIM PODEMOS TER CONTROLE SOBRE TODAS AS POSIÇÕES DE TODAS AS EMBARCACOES CADASTRADAS
total_tipos_embarcacao = 3
numero_cadastro_atual = 0
while numero_cadastro_atual < total_tipos_embarcacao:
  total_embarcacoes = 0
  tamanho_embarcacao = 0
  quantidade_embarcacao_cadastrada = 0
  conteudo_embarcacao = 0
  if(numero_cadastro_atual == 0):
    total_embarcacoes = quantidade_porta_aviao
    tamanho_embarcacao = tamanho_porta_aviao
    conteudo_embarcacao = PORTA_AVIAO
  elif(numero_cadastro_atual == 1):
    total_embarcacoes = quantidade_cruzador
    tamanho_embarcacao = tamanho_cruzador
    conteudo_embarcacao = CRUZADOR
  else:
    total_embarcacoes = quantidade_fragata
    tamanho_embarcacao = tamanho_fragata
    conteudo_embarcacao = FRAGATA
  while quantidade_embarcacao_cadastrada < total_embarcacoes:
    os.system('cls||clear')
    desenhar_tabuleiro(matriz_valores)
    if(numero_cadastro_atual == 0):
      print(
          f'\n> Cadastre {total_embarcacoes-quantidade_embarcacao_cadastrada} porta-aviões')
    elif(numero_cadastro_atual == 1):
      print(
          f'\n> Cadastre {total_embarcacoes-quantidade_embarcacao_cadastrada} cruzadores')
    else:
      print(
          f'\n> Cadastre {total_embarcacoes-quantidade_embarcacao_cadastrada} fragatas')
    linha_embarcacao = input('\n>Digite a linha: ').upper()
    coluna_embarcacao = input('\n>Digite a coluna: ')
    if linha_embarcacao in linhas_matriz and coluna_embarcacao in colunas_matriz:
      linha_embarcacao = linhas_matriz.index(linha_embarcacao)
      coluna_embarcacao = int(coluna_embarcacao)
      posicao_disponivel = True
      for index_posicao_ocupada in range(tamanho_embarcacao):
        if(coluna_embarcacao+index_posicao_ocupada == 20 or matriz_valores[linha_embarcacao][coluna_embarcacao+index_posicao_ocupada] != '▮'):
          posicao_disponivel = False
          break
      if posicao_disponivel:
        for index_posicao_ocupada in range(tamanho_embarcacao):
          matriz_valores[linha_embarcacao][coluna_embarcacao +
                                           index_posicao_ocupada] = conteudo_embarcacao
        atualizar_posicoes_embarcacao(
            linha_embarcacao, coluna_embarcacao, numero_cadastro_atual, quantidade_embarcacao_cadastrada)
        quantidade_embarcacao_cadastrada += 1
      else:
        input('\n> Posição inválida, digite qualquer tecla para continuar...')
    else:
      input('\n> Posição inválida, digite qualquer tecla para continuar...')
  numero_cadastro_atual += 1

# ATAQUE

# FUNÇÃO QUE SERÁ CHAMADA QUANDO O USUÁRIO ESCOLHER UMA LINHA E UMA COLUNA PARA ATACAR
# A GRANDE SACADA DO ATAQUE ESTÁ NESSA FUNÇAO, POR EXEMPLO: DIGAMOS QUE HÁ UM PORTA AVIAO CADASTRADO NA LINHA A COLUNA 0 E O USUÁRIO ATACOU A LINHA A COLUNA 3, A COLUNA ATACADA POSSUI A ÚLTIMA PARTE DESSE PORTA AVIAO, O QUE ACONTECERÁ SERÁ O SEGUINTE:
# MATRIZ DAS POSICOES DO PORTA AVIAO ANTES DE SER ATACADA:
[[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [0, 0], [0, 0], [0, 0]], [
    [0, 0], [0, 0], [0, 0], [0, 0]]]
# MATRIZ DAS POSICOES DO PORTA AVIAO APÓS SER ATACADA:
[[[0, 0], [0, 1], [0, 2], NULL], [[0, 0], [0, 0], [0, 0], [0, 0]], [
    [0, 0], [0, 0], [0, 0], [0, 0]]]
# PERCEBA QUE A POSICAO DO ATAQUE NAO VAI EXISTIR MAIS E NO LUGAR DELA FICARÁ O VALOR NULL QUE SIGNIFICA VAZIO, QUANDO VAMOS COLOCANDO NULL NAS POSICOES QUE ESTÃO SENDO ATACADAS É POSSIVEL FAZER O CALCULO DOS PONTOS DO USUARIO POIS TODA VEZ QUE TIVER UM PORTA AVIAO COM 4 POSICOES NULAS, QUER DIZER QUE O MESMO NAUFRAGOU E O USUARIO RECEBEU 30 PONTOS, CASO TODAS AS POSICOES DE TODAS AS EMBARCACOES ESTIVEREM NULAS, SIGNIFICA QUE O JOGO ACABOU POIS O USUARIO NAUFRAGOU TODAS AS EMBARCACOES DO JOGO


def ataque(linha, coluna):
  embarcacao_atacada = False
  if(matriz_valores[linha][coluna] != '▮'):
    matriz_jogo[linha][coluna] = matriz_valores[linha][coluna]
    embarcacao_atacada = True
  else:
    matriz_jogo[linha][coluna] = 'X'
  if(not embarcacao_atacada):
    return
  tipo_embarcacao_atacada = int(matriz_valores[linha][coluna])
  todas_posicoes = [posicoes_fragata, posicoes_cruzador, posicoes_porta_aviao]
  for index_posicoes_embarcacao in range(len(todas_posicoes[tipo_embarcacao_atacada])):
    for index_embarcacao in range(len(todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao])):
      if(todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao] and
         todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao][0] == linha and
         todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao][1] == coluna):
        todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao] = NULL

# FUNCAO QUE NOS RETORNA A PONTUACAO FINAL DO JOGO, SERÁ ÚTIL PARA NÓS SABERMOS O FIM DO JOGO, POIS QUANDO O USUÁRIO ATINGIR A PONTUACAO FINAL SIGNIFICA QUE O JOGO ACABOU


def calcular_pontuacao_final():
  pontuacao = 0
  for index_pontuacao in range(len(pontuacoes)):
    if(index_pontuacao == 0):
      pontuacao += quantidade_fragata * pontuacoes[index_pontuacao]
    elif(index_pontuacao == 1):
      pontuacao += quantidade_cruzador * pontuacoes[index_pontuacao]
    else:
      pontuacao += quantidade_porta_aviao * pontuacoes[index_pontuacao]
  return pontuacao

# FUNCAO QUE CALCULA A PONTUACAO ATUAL DO USUARIO, ESSA FUNCAO VERIFICA AS POSICOES DE TODAS AS EMBARCACOES E CASO ELA ENCONTRE 4 POSICOES NULAS NUM PORTA AVIAO POR EXEMPLO, SIGNIFICA QUE ESTÁ NAUFRAGADO, CASO ENCONTRE 2 POSICOES NULAS EM UMA FRAGATA TAMBÉM SIGNIFICA ISSO, CONFORME ELA VAI ENCONTRANDO EMBARCOES NAUFRAGADAS, A PONTUACAO DO USUARIO AUMENTA


def calcular_pontuacao_total():
  pontuacao = 0
  todas_posicoes = [posicoes_fragata, posicoes_cruzador, posicoes_porta_aviao]
  for tipo_embarcacao in range(3):
    for index_posicoes_embarcacao in range(len(todas_posicoes[tipo_embarcacao])):
      for index_embarcacao in range(len(todas_posicoes[tipo_embarcacao][index_posicoes_embarcacao])):
        embarcacao_naufragada = True
        if(todas_posicoes[tipo_embarcacao][index_posicoes_embarcacao][index_embarcacao] != NULL):
          embarcacao_naufragada = False
      if(embarcacao_naufragada):
        pontuacao += pontuacoes[tipo_embarcacao]
  return pontuacao


os.system('cls||clear')
# BLOCO DE CÓDIGO REFERENTE AO ATAQUE, EM VEZ DE USARMOS A matriz_valores que está preenchida e foi usada no cadastro, usamos a matriz_jogo que começará vazia e será atacada
# CONFORME OS ATAQUES VAO ACONTECENDO, AS POSICOES DAS EMBARCACOES VAO RECEBENDO NULL CASO SEJAM ATACADAS E A PONTUACAO DO USUARIO VAI SENDO CALCULADA A CADA REPETICAO DO WHILE
matriz_jogo = [0] * 20
for linha in range(len(matriz_jogo)):
  matriz_jogo[linha] = ['▮'] * 20
pontuacao_total = 0
pontuacao_final = calcular_pontuacao_final()
while True:
  os.system('cls||clear')
  desenhar_tabuleiro(matriz_jogo)
  print(f'\n>Pontuacao Total: {pontuacao_total}')
  if(pontuacao_final == pontuacao_total):
    input('\nParabéns, você venceu ! Digite qualquer tecla para finalizar o jogo...')
    break
  linha_ataque = input('\n>Digite a linha: ').upper()
  coluna_ataque = input('\n>Digite a coluna: ')
  if linha_ataque in linhas_matriz and coluna_ataque in colunas_matriz:
    linha_ataque = linhas_matriz.index(linha_ataque)
    coluna_ataque = int(coluna_ataque)
    posicao_disponivel = True
    if(matriz_jogo[linha_ataque][coluna_ataque] != '▮'):
      posicao_disponivel = False
    if posicao_disponivel:
      ataque(linha_ataque, coluna_ataque)
      pontuacao_total = calcular_pontuacao_total()
    else:
      input('\n> Posição inválida, digite qualquer tecla para continuar...')
  else:
    input('\n> Posição inválida, digite qualquer tecla para continuar...')
