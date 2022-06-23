import sqlite3
from contextlib import contextmanager

@contextmanager
def nova_conexao():
    conexao = sqlite3.connect('banco.db')
    createTable(conexao)
    try:
        yield conexao
    finally:       
        conexao.close()

def createTable(conexao):
    c = conexao.cursor()
    
    c.execute("""
    create table if not exists contatos(
    id integer primary key autoincrement,
    nome text,
    tel text,
    email text,
    senha text)
    """
    )
    
    conexao.commit()
    c.close()
