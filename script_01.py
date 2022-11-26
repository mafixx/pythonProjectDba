"""
Manipulação da tabela tb_contatos


"""

import sqlite3

if __name__ == "__main__":
    conexao = sqlite3.connect("db.sqlite3")

    # Inserir dados na tabela
    comando = """
    INSERT INTO tb_contatos (nome, sobrenome, telefone, email) VALUES (
        'Maria', 'das Graças', '4798913610', 'mariadasgracas@email.com' 
    )
    """

    # conexao.execute(comando)
    # conexao.commit()

    # Consultar dados na tabela

    comando = """
    SELECT * FROM tb_contatos
    """

    # Precisamos criar um cursor, que será o objeto que irá armazenar
    # os resultados trazidos da tabela
    cursor = conexao.cursor()
    resultado = cursor.execute(comando)

    # Podemos utilizar 3 métodos para acessar os resultados trazidos:
    # fetchone() -> retorna o elemento atual do cursor
    print(resultado.fetchone())

    # fetchmany(size) -> Retorna a quantidade de registros informada
    # no parâmetro size
    print(resultado.fetchmany(2))

    # fetchall() -> Retorna todos os registros restantes no cursor
    print(resultado.fetchall())


    # Atualizar dados na tabela
    comando = """
    UPDATE tb_contatos SET nome = 'João'
    """

    conexao.execute(comando)
    conexao.commit()

    # Excluir dados na tabela
    comando = """
    DELETE FROM tb_contatos WHERE id = 4
    """

    conexao.execute(comando)
    conexao.commit()