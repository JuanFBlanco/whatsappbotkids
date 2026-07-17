# Código escrito por: Juan Felipe Blanco Regueira
# Aplicação principal para administração do banco de dados tesourinha.db.
# ATENÇÃO!: CONTÉM INTERFACE DE TEXTO, IMPLEMENTAR INTERFACE GRAFICA NO FUTURO!!!

from models import(
    FuncionariosCRUD,
    ServicosCRUD,
    ResponsaveisCRUD,
    CriancasCRUD,
    HorariosCRUD,
    AgendamentosCRUD,
    MensagensCRUD
)

class SistemaTesourinha:

    def __init__(self):

        self.funcionarios = FuncionariosCRUD()
        self.servicos = ServicosCRUD()
        self.responsaveis = ResponsaveisCRUD()
        self.criancas = CriancasCRUD()
        self.horarios = HorariosCRUD()
        self.agendamentos = AgendamentosCRUD()
        self.mensagens = MensagensCRUD()

    def executar(self):

        while True:

            print("\n" + "=" * 50)
            print(" TESOURINHA DE BEZELA KIDS")
            print("=" * 50)

            print("1 = Funcionarios")
            print("2 - Serviços")
            print("3 - Responsáveis")
            print("4 - Crianças")
            print("5 - Horários")
            print("6 - Agendamentos")
            print("7 - Mensagens")
            print("0 - Sair")

            opcao = input("\nEscolha: ")

            if opcao == "1":
                self.menu_funcionarios()

            elif opcao == "2":
                self.menu_servicos()

            elif opcao == "3":
                self.menu_responsaveis()

            elif opcao == "4":
                self.menu_criancas()

            elif opcao == "5":
                self.menu_horarios()

            elif opcao == "6":
                self.menu_agendamentos()

            elif opcao == "7":
                self.menu_mensagens()

            elif opcao == "0":
                print("\nAté logo!")
                break
            
            else:
                print("\nOpção inválida!")

 # =====================================================

    def menu_funcionarios(self):
        self.menu_generico("Funcionários", self.funcionarios)

    def menu_servicos(self):
        self.menu_generico("Serviços", self.servicos)

    def menu_responsaveis(self):
        self.menu_generico("Responsáveis", self.responsaveis)

    def menu_criancas(self):
        self.menu_generico("Crianças", self.criancas)

    def menu_horarios(self):
        self.menu_generico("Horários", self.horarios)

    def menu_agendamentos(self):
        self.menu_generico("Agendamentos", self.agendamentos)

    def menu_mensagens(self):
        self.menu_generico("Mensagens", self.mensagens)

# =====================================================

    def menu_generico(self, titulo, crud):

     while True:
         print("\n" + "-" * 50)
         print(titulo.upper())
         print("-" * 50)

         print("1 - Listar")
         print("2 - Inserir")
         print("3 - Editar")
         print("4 - Excluir")
         print("0 - Voltar")

         opcao = input("\nEscolha: ")

         if opcao == "1":
             self.listar(crud)

         elif opcao == "2":
             print("\n(Será implementado)")

         elif opcao == "3":
             print("\n(Será implementado)")

         elif opcao == "4":
             print("\n(Será implementado)")

         elif opcao == "0":
             break

         else:
             print("Opção inválida!")

# =====================================================

    def listar(self, crud):

        registros = crud.listar()

        if not registros:
            print("\nNenhum registro encontrado.")
            return

        print()

        for registro in registros:
            print(dict(registro))


if __name__ == "__main__":

    sistema = SistemaTesourinha()
    sistema.executar()