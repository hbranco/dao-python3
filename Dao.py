#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql.cursors


class Dao:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.db_conexao = self.__connect(host, user, password, db)
        pass

    @staticmethod
    def __connect(host, user, password, db):
        '''
        configuração da conexão com o banco de dados
        MYSQL 5.4 +
        MariaDB 5.0 +
        :param host: hostname
        :param user:  user name database
        :param password: password do branco de dados
        :param db: database
        :return: connection
        '''
        try:
            connection = pymysql.connect(host, user, password, db, autocommit=False, connect_timeout=10, charset='utf8')
            return connection
        except pymysql.err.MySQLError as e:
            print(e)
            print("Erro ao conecctar com o banco de dados")
            return False

    # @staticmethod
    def select(self, campos, tabela, condicao=""):

        '''
        metodo para consultar no banco de dados
        :param campos: campos a serem buscados
        :param tabela:  tabela a ser consultada (pode conter joins)
        :param condicao: condição e busca (pode ser varia)
        :return: 
        '''

        with self.db_conexao.cursor() as cursor:
            try:
                if condicao:
                    query_busca = """ select {0} from {1} where {2}""".format(campos, tabela, condicao)
                    cursor.execute(query_busca)
                    query_resultado_consulta = cursor.fetchall()
                    return query_resultado_consulta

                else:
                    query_busca = """ select {0} from  {1}""".format(campos, tabela)
                    cursor.execute(query_busca)
                    query_resultado_consulta = cursor.fetchall()
                    return query_resultado_consulta

            except pymysql.MySQLError as e:
                print(e)
                print("Erro no select do banco")

    def insert(self, campos, tabela, dados):
        '''
        metodo para fazer inserção de dados no banco
        :param campos: campos da tabela
        :param tabela: tabela
        :param dados: dados
        :return:
        '''

        with self.db_conexao.cursor() as cursor:
            try:
                query_inserir = """ INSERT IGNORE INTO {0} ({1}) values ({2})""".format(tabela, campos, dados)
                print(query_inserir)
                cursor.execute(query_inserir)
                self.db_conexao.commit()
                return cursor.lastrowid
            except pymysql.MySQLError as e:
                print(e)
                print("Erro no insert do banco")

    def delete(self, tabela, condicao):
        '''
        metodo paara deletar um registro no banco
        :param tabela: seleciona a tabela
        :param condicao: condição de deleção
        :return:
        '''

        with self.db_conexao.cursor() as cursor:
            try:
                query_deleta = """ DELETE FROM {0} WHERE {1}""".format(tabela, condicao)
                print(query_deleta)
                cursor.execute(query_deleta)
                self.db_conexao.commit()
            except pymysql.MySQLError as e:
                print(e)
                print("Erro ao deletar do banco")

    def update(self, tabela, campos_dados, condicao):
        '''
        Metodo para fazer updade de um registo no banco
        :param tabela: tabela a ter o update
        :param campos_dados: campos a serem atualizados
        :param condicao: condição de atualização
        :return:
        '''
        with self.db_conexao.cursor() as cursor:
            try:
                query_inserir = """ UPDATE {0} SET {1} WHERE {2}""".format(tabela, campos_dados, condicao)
                print(query_inserir)
                cursor.execute(query_inserir)
                self.db_conexao.commit()
                return cursor.lastrowid
            except pymysql.MySQLError as e:
                print(e)
                print("Erro ao atulizar do banco")


    def execute_arbitraria(self, query, type):
        '''
        metodo para executar uma query arbitraria no banco..
        uma query mais complexa ou algo não previsto
        :param query: query a ser executada
        :param type: tipo da operação(SELECT,UPDATE,DELETE,REPLACE)
        :return: depende....
        '''

        print(query, type)


        if type == "insert":
            with self.db_conexao.cursor() as cursor:
                try:
                    cursor.execute(query)
                    self.db_conexao.commit()
                    return cursor.lastrowid
                    pass
                except pymysql.MySQLError as e:
                    print(e)
                    print("Erro ao utilizar o metodo execute_arbitraria()")



        pass