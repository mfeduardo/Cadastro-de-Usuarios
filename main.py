# Principal
from sistema import telas as tela

if __name__ == '__main__':
    menu = 5

    tela.apresentacao()

    while menu != 4:
        tela.rodape()
    
        menu = input(' /// [1] Cadastrar [2] Listar [3] Pesquisar [4] Sair: ')

        if menu.isdigit():
            
            menu = int(menu)
            
            if menu in range(1, 4):
                tela.funcoes[menu]()
        