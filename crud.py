import psycopg2

class AppBD:
    def __init__(self):
        print("Método construtor")

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="Pass@Word001", host="127.0.0.1", port="5432", database="postgres")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar com o banco", error)

    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = """SELECT * FROM produto"""

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)
        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi fechada")
        return registros

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            postgres_insert_query = """INSERT INTO produto (CODIGO, NOME, PRECO) VALUES (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)

            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            print("Falha ao inserir dados na tabela", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi fechada")

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registros antes da atualização")
            sql_select_query = """SELECT * FROM produto WHERE CODIGO = %s"""

            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)

            sql_update_query = """UPDATE produto SET nome = %s, preco = %s, WHERE codigo = %s"""
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso")
            print("Registro depois da atualização")
            sql_select_query = """SELECT * FROM produto WHERE codigo = %s"""
            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Falha ao atualizar dados", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi fechada")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            sql_delete_query = """DELETE FROM produto WHERE codigo = %s"""
            cursor.execute(sql_delete_query, (codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso")
        except (Exception, psycopg2.Error) as error:
            print("Erro na exclusão", error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi fechada")