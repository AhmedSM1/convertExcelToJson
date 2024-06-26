import pandas as pd
import json




def json_to_sql_file(json_file_path, sql_file_path, table_name):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Generate SQL insert statements
    sql_statements = []
    for record in data:
        print(record)
        columns = ', '.join(record.keys())
        values = ', '.join(["'{}'".format(str(value).replace("'", "''")) if isinstance(value, str) else str(value) for value in record.values()])
        sql_statements.append("INSERT INTO {} ({}) VALUES ({});".format(table_name, columns, values))
    
    # Write SQL statements to file
    with open(sql_file_path, 'w') as file:
        file.write('\n'.join(sql_statements))

# # Load the Excel file
# excel_file_path = 'random.xlsx'
# sheet_name = 'data'  # Change this to your sheet name if necessary
# json_file_path = 'data.json'
# columns_to_convert = ['msisdn'] 
# excel_to_json(excel_file_path, json_file_path, columns_to_convert)


# Usage example
json_file_path = 'data.json'
sql_file_path = 'data.sql'
table_name = 'MSISDN'
json_to_sql_file(json_file_path, sql_file_path , table_name)