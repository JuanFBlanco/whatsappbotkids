# Código criado por: Juan Felipe Blanco Regueira
# Código criado para o projeto TESOURINHA DE BELEZA KIDS, este código é responsável por criar o banco de dados
# e as tabelas necessárias para o funcionamento do sistema de agendamentos, futuramente será integrado a um
# chatbot que irá interagir com o usuário e realizar os agendamentos de forma automatizada.

import sqlite3

#conecta ao banco de dados, cria caso não exista um.
conn = sqlite3.connect('tesourinha.db')

#ativa o suporte a chaves estrangeiras
conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()

#====================================
# Tabela Funcionários
#====================================
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    funcao TEXT NOT NULL,
    horario_trabalho TEXT NOT NULL
)
''')

#====================================
# Tabela Serviços
#====================================
cursor.execute('''
CREATE TABLE IF NOT EXISTS servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_servico TEXT NOT NULL,
    valor REAL NOT NULL
)
''')

#====================================
# Tabela Responsavéis
#====================================
cursor.execute('''
CREATE TABLE IF NOT EXISTS responsaveis(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL,
    endereco TEXT NOT NULL,
    email TEXT
)
''')

#====================================
# Tabela Crianças
#====================================
cursor.execute('''
CREATE TABLE IF NOT EXISTS criancas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    responsavel_id INTEGER NOT NULL,
    FOREIGN KEY (responsavel_id) REFERENCES responsaveis(id) ON DELETE CASCADE
)
''')

#====================================
# Tabela Agendamentos
#====================================
cursor.execute('''
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crianca_id INTEGER NOT NULL,
    servico_id INTEGER NOT NULL,
    funcionario_id INTEGER NOT NULL,
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (crianca_id) REFERENCES criancas(id) ON DELETE CASCADE,
    FOREIGN KEY (servico_id) REFERENCES servicos(id) ON DELETE CASCADE,
    FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id) ON DELETE CASCADE
)
''')

conn.commit()
conn.close()

print("Banco de dados e tabelas criados com sucesso!")