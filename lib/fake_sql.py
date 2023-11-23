from heroes_database import heroes
from users_database import users

database = {}
query = input("Q: ")

USERS = users()
HEROES = heroes()

TABLE_MAPPING = {
    "USERS": USERS,
    "HEROES": HEROES
}

def Main(query=query):
    query = query.strip().upper()
    split_query = query.split() + [";"] if not query.endswith(";") else query.split()

    if not query.strip():
        raise ValueError("No query was created")
    if "SELECT" not in split_query or "FROM" not in split_query:
        raise ValueError("Incorrect syntax")
    if not query.endswith(";"):
        raise ValueError("Missing a semicolon")
    print("Deu certo.")
    
    from_result = FROM(table=split_query[3].rstrip(";"))
    select_result = SELECT(columns=split_query[1], result=from_result)
    if split_query[2] == "FROM":
        from_result
    if split_query[0] == "SELECT":
        select_result
    if "WHERE" in split_query:
        if split_query[4] == "WHERE":
            WHERE(
                condition=[x.lower() for x in split_query[4:]], 
                select_result=select_result
            )
    else:
        raise ValueError("WHERE clause not found.")


def SELECT(columns, result):
    columns = columns.strip().upper()
    if columns == "*":
        return result
    else:
        columns = columns.split(",")
        for row in result:
            cols_data = {}
            for col in row:
                if col.upper() in columns:
                    cols_data[col] = row[col]
            return cols_data
    

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


def WHERE(condition, select_result):
    split_condition = condition
    
    filtered_result = []
    
    if split_condition[2] == "<":        
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value < float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        print(filtered_result)
        return 
            
    if split_condition[2] == "=":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value == float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        print(filtered_result)
        return
    
    if split_condition[2] == ">":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value > float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        print(filtered_result)
        
    if split_condition[2] == "<=" or split_condition[2] == "=<":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value <= float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        print(filtered_result)
        return
    
    if split_condition[2] == ">=" or split_condition[2] == "=>":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value >= float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        print(filtered_result)
        return
    
Main()
