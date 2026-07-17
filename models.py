#Código escrito por: Juan Felipe Blanco Regueira
#Código para criar uma cada adicional de abstração para seguir o principio de responsabilidade única (SRP).

from crud import BaseCRUD

class FuncionariosCRUD(BaseCRUD):
    def __init__(self):
        super().__init__("funcionarios")

    def buscar_por_funcao(self, funcao):
        return self.buscar("funcao", funcao)
    
class ServicosCRUD(BaseCRUD):
    def __init__(self):
        super().__init__("servicos")
    
    def buscar_por_nome(self, nome):
        return self.buscar("nome_servico", nome)

class ResponsaveisCRUD(BaseCRUD):
    def __init__(self):
        super().__init__("responsaveis")

    def buscar_por_telefone(self, telefone):
        self.db.conectar()

        try:
            return self.db.consultar_um(
                """
                SELECT *
                FROM responsaveis
                WHERE telefone=?
                """,
                (telefone,)
            )
        
        finally:
            self.db.desconectar()

class CriancasCRUD(BaseCRUD):
    def __init__(self):
        super().__init__("criancas")

    def listar_por_responsavel(self, responsavel_id):
        self.db.conectar()

        try:
            return self.db.consultar(
                """
                SELECT *
                FROM crincas
                WHERE responsavel_id=?
                ORDER BY nome
                """,
                (responsavel_id,)
            )
        
        finally:
            self.db.desconectar()

class HorariosCRUD(BaseCRUD):
    def __init__(self):
        super().__init__("horarios")

    def listar_disponiveis(self):
        self.db.conectar()

        try:
            return self.db.consultar(
                """
                SELECT *
                FROM horarios
                WHERE satus = 'Disponível'
                ORDER by data_hora
                """
            )
        
        finally:
            self.db.desconectar()

class AgendamentosCRUD(BaseCRUD):
    def __init__(self):
        super().__init__("agendamentos")

    def listar_agendados(self):
        self.db.conectar()

        try:
            return self.db.consultar(
                """
                SELECT *
                FROM agendamentos
                WHERE satus = 'Agendado'
                """
            )
        
        finally:
            self.db.desconectar()

class MensagensCRUD(BaseCRUD):
    def __init__(self):
        super().__init__("mensagens")
          