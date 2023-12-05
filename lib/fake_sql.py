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
    select_result = SELECT(columns=split_query[1].upper(), table=from_result)
    if not split_query[2] == "FROM":
        raise ValueError("Syntax error.")
    if not split_query[0] == "SELECT":
        raise ValueError("Wrong index")
    if "WHERE" in split_query:
        if split_query[4] == "WHERE":
            return WHERE(
                condition=[x.lower() for x in split_query[4:]], 
                select_result=select_result
            )
    else:
        return select_result



def SELECT(columns, table):
    columns = columns.strip().upper()
    if columns == "*":
        return table
    else:
        selected_data = []
        columns = columns.split(",")
        
        table_keys = [list(dct.keys()) for dct in table]
        print(table_keys)
        for x in columns:
            x = x.strip().lower()
            if not any(x in keys for keys in table_keys):
                raise ValueError("This column does not exist.")
        
        for row in table:
            cols_data = {}
            for col in row:
                if col.upper() in columns:
                    cols_data[col] = row[col]
            selected_data.append(cols_data)
        return selected_data


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
        return filtered_result
            
    if split_condition[2] == "=":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value == float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        return filtered_result
    
    if split_condition[2] == ">":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value > float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        return filtered_result
        
    if split_condition[2] == "<=" or split_condition[2] == "=<":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value <= float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        return filtered_result
    
    if split_condition[2] == ">=" or split_condition[2] == "=>":
        for row in select_result:
            cell_value = row[split_condition[1]]
            
            if cell_value >= float(split_condition[3].rstrip(";")):
                filtered_result.append(row)
        return filtered_result
    
# Main()
