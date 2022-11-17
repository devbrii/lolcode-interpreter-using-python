import re
import os
os.system('cls')

from prettytable import PrettyTable

# read file
def input_file(file_name):
  with open(file_name) as file_in:
    lines = []
    for line in file_in:
      line = line.strip() # removes \n
      lines.append(line)

    file_in.close()

  return lines

def has_duplicate(lexeme, symbol_table):
  in_symbol_table = False
  for item in symbol_table:
    if item['lexeme'] == lexeme:
      return not in_symbol_table

  return in_symbol_table

def lexeme_match(symbol_table, regex_pattern, lexeme_type, line):
  print(f"OLD LINE: {line}")
  lexeme = re.findall(regex_pattern, line)
  if lexeme:
    for item in lexeme:
      if not has_duplicate(item, symbol_table):
        symbol_table.append({ "lexeme": item, "type": lexeme_type })
  print(f"NEW LINE: {line}")

  return line

lines = input_file('test_cases/sample.lol')
keywords = input_file('interpreter_files/keywords.txt') 
operators = input_file('interpreter_files/operators.txt') 
symbol_table = []


for line in lines:
  # checks for keyword
  for keyword in keywords:
    line = lexeme_match(symbol_table, rf'\b{keyword}\b', "Keyword", line)

  # checks for operators
  for operator in operators:
    line = lexeme_match(symbol_table, rf'\b{operator}\b', "Operator", line)

  # checks all integers
  line = lexeme_match(symbol_table, r'(?<!\.)\b[0-9]+\b(?!\.)', "Integer", line)
  
  # checks float 
  line = lexeme_match(symbol_table, r'\b\d+?\.\d+\b', "Float", line)

  # variable
  line = lexeme_match(symbol_table, fr'{line}', "Variable Identifier", line)

mylist = list( dict.fromkeys(symbol_table) )
print(mylist)

# output file
pretty_table = PrettyTable()
pretty_table.field_names = ["Lexeme", "Type"]

for symbol in mylist:
  pretty_table.add_row([symbol['lexeme'], symbol['type']])

print(pretty_table)

  # print(symbol)

# for symbol in symbol_table:
#   print(symbol)