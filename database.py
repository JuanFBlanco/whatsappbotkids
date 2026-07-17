# Codigo escrito por: Juan Felipe Blanco Regueira
# Código que cria uma camada de conexão ao banco de dados para o programa de sistema administrativo do banco de dados TesourinhaDB.

import sqlite3

class Database:
    def _init_(self, banco="tesourinha.db"):
        self.banco = banco
        self.conn = None
        self.cursor = None

    def conectar(self):
        """Abre conexão com o banco."""
        if self.conn is None:
            self.conn = sqlite3.connect(self.banco)
            self.conn.execute("PRAGMA foreign_keys = ON")
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()

    def desconectar(self):
        """Fecha a conexão com o banco."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def commit(self):
        """Confirma alterações nas tabelas."""
        if self.conn:
            self.conn.commit()

    def rollback(self):
        """Desfaz alterações nas tabelas."""
        if self.conn:
            self.conn.rollback()

    def executar(self, sql, parametros=()):
        """Executa INSET, UPDATE e DELETE."""
        self.cursor.execute(sql, parametros)
        self.commit()

    def consultar(self, sql, parametros=()):
        """Executa SELECT retornando todos os registros."""
        self.cursor.execute(sql, parametros)
        return self.cursor.fetchall()
    
    def consultar_um(self, sql, parametros=()):
        """Executa SELECT retornando apenas um registro."""
        self.cursor.execute(sql, parametros)
        return self.cursor.fetchone()
    
    def ultimo_id(self):
        """Retorna o ID do ultimo INSERT."""
        return self.cursor.lastrowid
    