import json
from fake_sql import Main

dict_list = Main()

file_name = "query.json"

with open(file_name, "w") as json_file:
    json.dump(dict_list, json_file, indent=4)

# Create HTML table
with open(file_name, "r") as file:
    data = json.load(file)
    
html_table = '<table border="1">\n<tr>'
# Cabeçalhos da tabela
html_table += ''.join(f'<th>{key}</th>' for key in data[0].keys())
html_table += '</tr>\n'

# Linhas da tabela
for row in data:
    html_table += '<tr>'
    html_table += ''.join(f'<td>{value}</td>' for value in row.values())
    html_table += '</tr>\n'

html_table += '</table>'

# Escrever o código HTML em um arquivo
with open('table.html', 'w') as html_file:
    html_file.write(html_table)