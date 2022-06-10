from asyncio.windows_events import NULL
import os
matriz_valores = [0] * 20
linhas_matriz = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
colunas_matriz = ['0', '1', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
for linha in range(len(matriz_valores)):
  matriz_valores[linha] = ['▮'] * 20
# quantidadePortaAviao = 3
# tamanhoPortaAviao = 4
# quantidadeCruzador = 4
# tamanhoCruzador = 3
# quantidadeFragata = 5
# tamanhoFragata = 2
PORTA_AVIAO = '2'
CRUZADOR = '1'
FRAGATA = '0'
quantidade_porta_aviao = 1
tamanho_porta_aviao = 4
posicoes_porta_aviao = []

quantidade_cruzador = 1
tamanho_cruzador = 3
posicoes_cruzador = []

quantidade_fragata = 1
tamanho_fragata = 2
posicoes_fragata = []

posicoes_porta_aviao = []
posicoes_cruzador = []
posicoes_fragata = []
pontuacoes = [10, 20, 30]


def calcularPontuacaoFinal():
  pontuacao = 0
  for index_pontuacao in range(len(pontuacoes)):
    if(index_pontuacao == 0):
      pontuacao += quantidade_fragata * pontuacoes[index_pontuacao]
    elif(index_pontuacao == 1):
      pontuacao += quantidade_cruzador * pontuacoes[index_pontuacao]
    else:
      pontuacao += quantidade_porta_aviao * pontuacoes[index_pontuacao]
  return pontuacao


def calcularPosicoesEmbarcacao(tipo_embarcacao):
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


for index_tipo_embarcacao in range(3):
  if(index_tipo_embarcacao == 0):
    posicoes_fragata = calcularPosicoesEmbarcacao(index_tipo_embarcacao)
  elif index_tipo_embarcacao == 1:
    posicoes_cruzador = calcularPosicoesEmbarcacao(index_tipo_embarcacao)
  else:
    posicoes_porta_aviao = calcularPosicoesEmbarcacao(index_tipo_embarcacao)


def atualizarPosicoesEmbarcacao(linha, coluna, tipo_embarcacao, index_embarcacao):
  todas_posicoes = [posicoes_porta_aviao, posicoes_cruzador, posicoes_fragata]
  for index_posicao in range(len(todas_posicoes[tipo_embarcacao][index_embarcacao])):
    todas_posicoes[tipo_embarcacao][index_embarcacao][index_posicao] = [
        linha, coluna+index_posicao]

# CADASTRO DE EMBARCAÇÕES


os.system('cls||clear')

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
    for linha in range(len(matriz_valores)):
      if(linha == 0):
        print(
            '\n  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19')
      for coluna in range(20):
        if(coluna == 0):
          print(
              f'{linhas_matriz[linha]} {matriz_valores[linha][coluna]}  ', end='')
        elif (coluna == 19):
          print(f'{matriz_valores[linha][coluna]}')
        else:
          print(f'{matriz_valores[linha][coluna]}  ', end='')
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
        atualizarPosicoesEmbarcacao(
            linha_embarcacao, coluna_embarcacao, numero_cadastro_atual, quantidade_embarcacao_cadastrada)
        quantidade_embarcacao_cadastrada += 1
      else:
        input('\n> Posição inválida, digite qualquer tecla para continuar...')
    else:
      input('\n> Posição inválida, digite qualquer tecla para continuar...')
  numero_cadastro_atual += 1

# ATAQUE


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
  # print(f'\n> Tipo embarcacao {tipo_embarcacao_atacada}')
  # print(f'\n> INDEX POSICOES EMBARCACAO {todas_posicoes[tipo_embarcacao_atacada]}')
  for index_posicoes_embarcacao in range(len(todas_posicoes[tipo_embarcacao_atacada])):
    for index_embarcacao in range(len(todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao])):
      # print(f'TESTE {todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao]}')
      # print(f'LINHA ATACADA {linha}')
      # print(f'COLUNA ATACADA {coluna}')
      if(todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao] and
         todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao][0] == linha and
         todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao][1] == coluna):
        todas_posicoes[tipo_embarcacao_atacada][index_posicoes_embarcacao][index_embarcacao] = NULL


def calcularPontuacao():
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

matriz_jogo = [0] * 20
for linha in range(len(matriz_jogo)):
  matriz_jogo[linha] = ['▮'] * 20
pontuacao_total = 0
pontuacao_final = calcularPontuacaoFinal()
fim_jogo = False
while not fim_jogo:
  os.system('cls||clear')
  for linha in range(len(matriz_jogo)):
    if(linha == 0):
      print(
          '\n  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19')
    for coluna in range(20):
      if(coluna == 0):
        print(
            f'{linhas_matriz[linha]} {matriz_jogo[linha][coluna]}  ', end='')
      elif (coluna == 19):
        print(f'{matriz_jogo[linha][coluna]}')
      else:
        print(f'{matriz_jogo[linha][coluna]}  ', end='')
  if(pontuacao_final == pontuacao_total):
    fim_jogo = True
    input('\nParabéns, você venceu ! Digite qualquer tecla para finalizar o jogo...')
    break
  print(f'\n>Pontuacao Total: {pontuacao_total}')
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
      pontuacao_total = calcularPontuacao()
    else:
      input('\n> Posição inválida, digite qualquer tecla para continuar...')
  else:
    input('\n> Posição inválida, digite qualquer tecla para continuar...')
