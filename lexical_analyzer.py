import re
import os
os.system('cls')

# read file
def input_file(file_name):
  with open(file_name) as file_in:
    lines = []
    for line in file_in:
      line = line.strip() # removes \n
      lines.append(line)

  return lines

def has_duplicate(lexeme, symbol_table):
  in_symbol_table = False
  for item in symbol_table:
    if item['lexeme'] == lexeme:
      return not in_symbol_table

  return in_symbol_table


def lexeme_match(symbol_table, regex_pattern, type, line):
  lexeme = re.findall(regex_pattern, line)
  if lexeme:
    for i in lexeme:
      if not has_duplicate(i, symbol_table):
        symbol_table.append({ "lexeme": i, "type": type })


lines = input_file('files/input.lol')
keywords = input_file('files/keywords.txt') 
symbol_table = []

for line in lines:
  for keyword in keywords:
    lexeme_match(symbol_table, rf'\b{keyword}\b', "Keyword", line)

  lexeme_match(symbol_table, r'(?<!\.)\b[0-9]+\b(?!\.)', "Integer", line)
  lexeme_match(symbol_table, r'\b\d+?\.\d+\b', "Float", line)

for symbol in symbol_table:
  print(symbol)