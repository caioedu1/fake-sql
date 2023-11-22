from heroes_database import heroes
from users_database import users

database = {}
query = input("Q: ")

# Objetivo 1:
# SELECT name, age FROM users;
USERS = users()
HEROES = heroes()

TABLE_MAPPING = {
    "USERS": USERS,
    "HEROES": HEROES
}

"""
TO DOs
1. Verificar e corrigir por erros de syntax no código `SELECT name,age FROM users;`
2. Permitir a separação de listagem de colunas printadas `SELECT name, age FROM users;`
3. Iniciar a cláusula WHERE
"""

def query_clean(query=query):
    query = query.strip().upper()
    split_query = query.split() + [";"] if not query.endswith(";") else query.split()

    if not query.strip():
        raise ValueError("No query was created")
    if "SELECT" not in split_query or "FROM" not in split_query:
        raise ValueError("Incorrect syntax")
    if not query.endswith(";"):
        raise ValueError("Missing a semicolon")
    print("Deu certo.")
    
    fromfunc_return = FROM(table=split_query[3].rstrip(";"))
    if split_query[2] == "FROM":
        fromfunc_return
    if split_query[0] == "SELECT":
        SELECT(columns=split_query[1], result=fromfunc_return)


def SELECT(columns, result):
    columns = columns.strip().upper()
    # 1. verificar se argumento select é *
    #   a. Se sim, printar todas as tabelas do database selecionado pela função FROM. -> check
    #   b. Se não, verificar quais colunas são o argumento.
    # 2. verificar colunas especificadas no argumento.
    #   a. printar de acordo com as colunas.
    if columns == "*":
        print(result)
    else:
        columns = columns.split(",")
        # passar por todas as colunas e printar somente as que o nome batem com o input do usuário
        for row in result:
            cols_data = {}
            for col in row:
                if col.upper() in columns:
                    cols_data[col] = row[col]
            print(cols_data)
    

def FROM(table):
    if not table:
        raise ValueError("Table must be specified")
    if table != "users".upper() and table != "heroes".upper():
        raise ValueError("This table does not exist")
    if table not in TABLE_MAPPING:
        raise ValueError("This table does not exist")
    
    database = TABLE_MAPPING[table]
    print("Deu certo 2.")
    
    return database

def WHERE(condition):
    pass
    
query_clean()
