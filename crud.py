#Código escrito por: Juan Felipe Blanco Regueira
#Criação de uma classe de CRUD utilizando a camada de conexão com o banco de dados criado em databade.py.

from database import Database

class BaseCRUD:
    """Classe base para operações CRUD em qualquer tabela."""
    
    def __init__(self, tabela):
        self.db = Database()
        self.tabela = tabela

    #=======================================
    # CREATE
    #=======================================
    def inserir(self, dados):
        """
        dados={
            "nome": "Ana",
            "funcao": "Cabeleleira"
        }
        """

        campos = ", ".join(dados.keys())
        placeholders = ", ".join(["?"] * len(dados))
        valores = tuple(dados.values())

        sql = f"""
         INSERT INTO {self.tabela}
         ({campos})
         VALUES ({placeholders})
         """
        
        self.db.conectar()

        try:
            self.db.executar(sql, valores)
            return self.db.ultimo_id()
        
        finally:
            self.db.desconectar()

    #======================================
    # READ
    #======================================

    def listar(self):
        self.db.conectar()

        try:
            sql = f"SELECT * FROM {self.tabela}"
            return self.db.consultar(sql)
        
        finally:
            self.db.desconectar()

    def buscar_por_id(self, id_registro):

        self.db.conectar()

        try:
            sql = f"""
             SELECT *
             FROM {self.tabela}
             WHERE id = ?
             """
            
            return self.db.consultar_um(sql, (id_registro,))
        
        finally:
            self.db.desconectar()

    def buscar(self, campo, valor):

        self.db.conectar()

        try:
            sql = f"""
             SELECT *
             FROM {self.tabela}
             WHERE {campo} LIKE ?
             """
            
            return self.db.consultar(sql, (f"%{valor}%",))
        
        finally:
            self.db.desconectar()

    #=====================================
    # UPDATE
    #=====================================

    def atualizar(self, id_registro, dados):

        campos= ", ".join(
            [f"{campo}=?" for campo in dados.keys()]
        )

        valores = list(dados.values())
        valores.append(id_registro)

        sql = f"""
         UPDATE {self.tabela}
         SET {campos}
         WHERE id=?
         """
        
        self.db.conectar()

        try:
            self.db.executar(sql, tuple(valores))

        finally:
            self.db.desconectar()

    #====================================
    # DELETE
    #====================================

    def excluir(self, id_registro):

        sql = f"""
         DELETE FROM {self.tabela}
         WHERE id=?
         """

        self.db.conectar()

        try:
            self.db.executar(sql, (id_registro,))

        finally:
            self.db.desconectar()