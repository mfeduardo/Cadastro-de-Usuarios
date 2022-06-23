# Operações I/O
from sistema import telas as tela
from sistema import secure_password_input, Crud


def cadastrar():
    sessao = '[1] CADASTRO DE CLIENTE'

    tela.tela_sessao(sessao)

    nome, tel, email, senha, senha_conferir = input('\n Nome: '), input(' Telefone: '), input(
        ' E-mail: '), secure_password_input(' Senha: '), secure_password_input(' Repetir Senha: ')

    while senha != senha_conferir:

        print('\n Senhas não conferem! Por favor, informe a senha novamente. \n')

        senha, senha_conferir = secure_password_input(
            ' Senha: '), secure_password_input(' Conferir Senha: ')

    dados = {}

    dados['nome'], dados['tel'], dados['email'], dados['senha'] = nome.strip(
    ), tel.strip(), email.strip(), senha.strip()

    if nome:
        usuario = Crud()
        usuario.inserirUsuario(dados['nome'], dados['tel'], dados['email'], dados['senha'])
    else:
        print('\n Cliente não foi cadastrado: nome não informado!\n')


def listar():
    sessao = '[2] CLIENTES CADASTRADOS'

    tela.tela_sessao(sessao)

    usuarios = Crud()
    contatos = usuarios.selecionarUsuarios()
            
    for contato in contatos:
        print(
            f'\n Cod: {contato[0]}\n Nome: {contato[1]}\n Telefone: {contato[2]}\n Email: {contato[3]}')
            

    print(' ' + '-' * 70)

    print(f'\n >> Resultado(s): {len(contatos)}\n')


def pesquisar():
    sessao = '[3] PESQUISAR CADASTRO'

    tela.tela_sessao(sessao)
    
    nome = input('\n Nome do cliente: ')

    usuarios = Crud()
    contatos = usuarios.selecionarUsuario(nome)

    for contato in contatos:
        print(
                f'\n Cod: {contato[0]}\n Nome: {contato[1]}\n Telefone: {contato[2]}\n Email: {contato[3]}')
        id_referencia = contato[0]
    

    print(' ' + '-' * 70)
    resultados = len(contatos) if len(contatos) > 0 else 0
    
    print(f'\n >> Resultado(s): {resultados}\n')

    if resultados == 1:
        submenu(id_referencia, nome, contatos)
            

def submenu(id, nome, contatos):

    submenu = input('\n /// [D]eletar [E]ditar ')

    if submenu.lower() == 'd':
        confirmar_exclusao = input(
            '\n Confirma exclusão desse arquivo (s/n)? ')

        if confirmar_exclusao.lower() == 's':
            usuario = Crud()
            usuario.excluirUsuario(id)
            print(f'\n >> Cliente removido do cadastro!')
    
    elif submenu.lower() == 'e':
        
        for contato in contatos:
                print('\n Digite a nova informação ou tecle <<Enter>> para ignorar.')
                nome, tel, email = input(f'\n Nome: {contato[1]}: ') or contato[1], input(f' Telefone: {contato[2]}: ') or contato[2], input(f' E-mail: {contato[3]}: ') or contato[3]
                usuario = Crud()
                usuario.atualizarUsuario(contato[0], nome, tel,email)

