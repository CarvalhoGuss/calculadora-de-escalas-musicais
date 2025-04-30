import lib.sistema_notas


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: Por favor, digite uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


# Linha
def linha(tam=50):
    return '-' * tam


# Cabeçalho
def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


# Menu
def menu(lista, titulo):
    cabeçalho(f'\033[1:33m{titulo}\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m[{c}]\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mDigite o número da opção que deseja: \033[m')
    print()
    return opc


def lista_de_escalas():
    tupla_de_escalas = ['Escala Maior/Menor Natural', 'Escala Menor Harmônica', 'Escala Menor Melódica',
                        'Escala Pentatônica', 'Escala Blues (Penta-Blues)', 'Descreva uma escala']
    return tupla_de_escalas


def listas_modos_gregos():
    tupla_de_modos = ['Jônio - Maior natural/diatônica', 'Dórico', 'Frígio', 'Lídio', 'Mixolídio',
                      'Eólio - Escala Menor Natural', 'Lócrio']
    return tupla_de_modos


def listas_modos_gregos_menor_harmonico():
    # Lista de modos gregos menores harmonicos
    tupla_de_modos_gregos_menor_harmonico = ['Modo Eólio com Sétima Maior (Modo Harmônico Menor)',
                                             'Modo Lócrio Natural 6 (Modo Lócrio #6)',
                                             'Modo Jônio #5 (Modo Maior Aumentado)',
                                             'Modo Dórico #4 (Modo Dórico Aumentado)',
                                             'Modo Frígio Dominante (Modo Frígio Maior)',
                                             'Modo Lídio #2 (Modo Lídio Aumentado #2)',
                                             'Modo Superlócrio (Modo Diminuto)']
    return tupla_de_modos_gregos_menor_harmonico


def escolha_escala(resposta1, nota_do_menu):
    # Exibe o menu para Calcular uma escala
    resposta2_str = lista_de_escalas()
    resposta2 = lib.interface.menu(resposta2_str, 'Calcular uma escala')
    return resposta2_str, resposta2


def escala_maiormenor_natural(resposta2, resposta2_str, nota_do_menu):
    # Escala Maior/Menor Natural
    resposta3_str = listas_modos_gregos()
    resposta3 = lib.interface.menu(resposta3_str, 'Escala Maior/Menor Natural')
    # Menu citando a escala.
    resposta4 = lib.interface.menu([*lib.sistema_notas.escala_cromatica()], resposta3_str[resposta3 - 1])
    # Chama a função de cálculo da escala e exibe o resultado
    lib.interface.informacaoescala(nota_do_menu[resposta4 - 1], resposta2_str[resposta2 - 1],
                                   resposta3_str[resposta3 - 1], resposta4)


def escala_menor_harmonica(resposta2, resposta2_str, nota_do_menu):
    # Escala Menor Harmonica
    resposta3_str = listas_modos_gregos_menor_harmonico()
    resposta3 = lib.interface.menu(resposta3_str, 'Escala Menor Harmônica')
    # Menu citando a escala.
    resposta4 = lib.interface.menu([*lib.sistema_notas.escala_cromatica()], resposta3_str[resposta3 - 1])
    # Chama a função de cálculo da escala e exibe o resultado
    lib.interface.informacaoescala(nota_do_menu[resposta4 - 1], resposta2_str[resposta2 - 1],
                                   resposta3_str[resposta3 - 1], resposta4)


def escala_menor_melodica(resposta2, resposta2_str, nota_do_menu):
    # Escala Menor Melódica
    resposta3_str = listas_modos_gregos_menor_harmonico()
    resposta3 = lib.interface.menu(resposta3_str, 'Escala Menor Melódica')
    # Menu citando a escala.
    resposta4 = lib.interface.menu([*lib.sistema_notas.escala_cromatica()], resposta3_str[resposta3 - 1])
    # Chama a função de cálculo da escala e exibe o resultado
    lib.interface.informacaoescala(nota_do_menu[resposta4 - 1], resposta2_str[resposta2 - 1],
                                   resposta3_str[resposta3 - 1], resposta4)



def informacaoescala(tom_da_escala, nome_da_escala, modo, numero_nota):
    print(linha())
    print(f'\033[1:33mEscala de {tom_da_escala} {nome_da_escala} selecionada\033[m')
    print(f'\033[1:33mModo {modo} selecionado\033[m')
    print(linha())
    if nome_da_escala == 'Escala Maior/Menor Natural':
        formula_geral, estrutura = lib.sistema_notas.formula_da_escala(modo)
        escala_final = lib.sistema_notas.calculo_escala(estrutura, numero_nota)
    elif nome_da_escala == 'Escala Menor Harmônica':
        formula_geral, estrutura = lib.sistema_notas.formula_da_escala_menor_harmonica(modo)
        escala_final = lib.sistema_notas.calculo_escala(estrutura, numero_nota)
    elif nome_da_escala == 'Escala Menor Melódica':
        formula_geral, estrutura = lib.sistema_notas.formula_da_escala_menor_melodica(modo)
        escala_final = lib.sistema_notas.calculo_escala(estrutura, numero_nota)
    print(f'\033[1:33m{formula_geral}\033[m')
    print()
    print(f'\033[1:32m{escala_final}\033[m')
    print()
    print()
