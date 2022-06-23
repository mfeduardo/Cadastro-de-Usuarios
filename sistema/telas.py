# Display
import os
from sistema import operacoes as op

moldura = '='
cabecalho_area = 70
cabecalho_titulo = ' SISTEMA DE CADASTRO DE USUÁRIOS (v. 1.7) '
funcoes = ['', op.cadastrar, op.listar, op.pesquisar]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho():
    area = int((cabecalho_area - len(cabecalho_titulo)) / 2)

    print()

    cabecalho = moldura * area + cabecalho_titulo + moldura * area

    print(' ' + cabecalho)


def rodape():
    moldura_rodape = moldura * cabecalho_area + '\n'

    print(' ' + moldura_rodape)


def tela_sessao(sessao):
    clear()

    cabecalho()

    display = '>>> ' + sessao

    print('\n' + ' ' + display)


def apresentacao():
    clear()

    cabecalho()

    print("""
     [1] Cadastrar
     [2] Listar
     [3] Pesquisar
     [4] Sair
""")
