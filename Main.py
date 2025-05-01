# Descrição: Este módulo calcula a escala musical com todas as notas que compõem as principais escalas.
# Autor: Gustavo Carvalho Brito
# Data de criação: 07/09/2023
# Última Modificação: 04/04/2023

from time import sleep
import lib.interface
import lib.sistema_notas

# Carrega todas as notas possiveis para serem usadas no menu
nota_do_menu = lib.sistema_notas.conjunto_notas_caculaveis()

# Loop principal do programa
while True:
    # Exibe o Menu Principal e captura a resposta do usuário
    resposta1 = lib.interface.menu(['Calcular uma escala.', 'Buscar uma escala.', 'Sair do programa.'],
                                  'CALCULADORA DE ESCALAS MUSICAIS')
    if resposta1 == 1:
        # Chama a função para escolher a escala
        resposta2_str, resposta2 = lib.interface.escolha_escala(resposta1, nota_do_menu)

        if resposta2 == 1:
            # Chama a função dque calcula e exibe o menu da escala maior/menor natural.
            lib.interface.escala_maiormenor_natural(resposta2, resposta2_str, nota_do_menu)

        elif resposta2 == 2:
            # Escala Menor Harmônica
            lib.interface.escala_menor_harmonica(resposta2, resposta2_str, nota_do_menu)

        elif resposta2 == 3:
            # Escala Menor Melódica
            lib.interface.escala_menor_melodica(resposta2, resposta2_str, nota_do_menu)
        elif resposta2 == 4:
            # Escala Pentatônica
            lib.interface.cabeçalho('\033[32mSaindo do programa...\033[m')
        elif resposta2 == 5:
            # Escala Blues (Penta-Blues)
            lib.interface.cabeçalho('\033[32mSaindo do programa...\033[m')
        elif resposta2 == 6:
            # Descrever uma escala
            lib.interface.cabeçalho('\033[32mSaindo do programa...\033[m')

    elif resposta1 == 2:
        # Opção de Buscar uma escala citando as notas
        lib.interface.cabeçalho('\033[32mSaindo do programa...\033[m')
    elif resposta1 == 3:
        # Opção de sair do Sistema
        lib.interface.cabeçalho('\033[32mSaindo do programa...\033[m')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)