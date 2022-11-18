from prettytable import PrettyTable
import re
import os
os.system('cls')


# read file

def input_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.strip()  # removes \n
            lines.append(line)

    return lines

def lexeme_match(symbol_table, regex_pattern, lexeme_type, line):
  lexeme = re.findall(regex_pattern, line)
  if lexeme:
    for item in lexeme:
        symbol_table.append({ "lexeme": item, "type": lexeme_type })

# def has_duplicate(lexeme, symbol_table):
# 	in_symbol_table = False
# 	for item in symbol_table:
#     	if item['lexeme'] == lexeme:
#       return not in_symbol_table

#   return in_symbol_table


lines = input_file('test_cases/sample.lol')
all_keywords = input_file('interpreter_files/all_keywords.txt')
general = input_file('interpreter_files/keywords.txt')
operators = input_file('interpreter_files/operators.txt')
symbol_table = []
updated_lines = []

for line in lines:
    # splits the line per word
    line_split = line.split()
    
    for keyword in all_keywords:
        keyword_split = keyword.split()
		
        if set(keyword_split).issubset(set(line_split)):
            updated_lines += list(set(line_split) - set(keyword_split))
            # print(keyword)
            if keyword in operators:
                symbol_table.append({"lexeme": keyword, "type": "Operator"})
            elif keyword in general:
                symbol_table.append({"lexeme": keyword, "type": "Keyword"})
        
        # if 

            # line_split = list(set(line_split) - set(keyword_split))

# print(updated_lines)
#  symbol_table.append({"lexeme": line, "type": "Variable Identifier" })


# output file
pretty_table = PrettyTable()
pretty_table.field_names = ["Lexeme", "Type"]

for symbol in symbol_table:
    pretty_table.add_row([symbol['lexeme'], symbol['type']])

print(pretty_table)
print(updated_lines)
# print(symbol)

# for symbol in symbol_table:
#   print(symbol)
