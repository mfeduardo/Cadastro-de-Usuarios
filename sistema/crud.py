from msilib.schema import Error
from .bd import nova_conexao
from hashlib import md5

class Crud:

    def inserirUsuario(self, nome, telefone, email, senha):
        with nova_conexao() as conexao:
            senha = senha.encode('utf8')
            cripto = md5(senha).hexdigest()
            try:
                cursor = conexao.cursor()
                cursor.execute("insert into contatos (nome, tel, email, senha) values ('" +  nome + "', '" + telefone + "', '" +  email + "', '" +   cripto + "' )")
                conexao.commit()
            except:
                print(f' Erro de inserção do registro!')
            else:
                print(
                    f' \n Cliente cadastrado com sucesso! (ID: {cursor.lastrowid})\n')

    def selecionarUsuarios(self):
        sql = 'SELECT * FROM contatos'

        with nova_conexao() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(sql)
                contatos = cursor.fetchall()
            except:
                print(f' Erro na consulta ao banco de dados!')
            else:
                return contatos

    def selecionarUsuario(self, nome):
        sql = "SELECT * FROM contatos WHERE nome LIKE '%"+ nome +"%'"

        if nome.isdigit():
            sql = "SELECT * FROM contatos WHERE id = "+ nome +""

        with nova_conexao() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(sql)
            except:
                print(f' Erro na consulta ao banco de dados!')
            else:
                resultado = [contato for contato in cursor]
                return resultado

    def atualizarUsuario(self, id, nome, telefone, email):
        args = (id,)
        sql = "UPDATE contatos SET nome = '" + nome + "',tel = '" + telefone + "', email = '" + email + "' where id = ? "
        
        with nova_conexao() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(sql, args)
                conexao.commit()
        
            except Error as e:
                print(f' Erro na na atualização do registro!', e)
            else:
                print(f'\n {cursor.rowcount} registro(s) atualizado(s).')
    
    def excluirUsuario(self, id):
        sql = "delete from contatos where id=?"
        args = (id,)
        with nova_conexao() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(sql, args)
                conexao.commit()
            except:
                print(f' Erro na na exclusão do registro!')
