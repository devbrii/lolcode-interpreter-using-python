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

def has_duplicate(lexeme):
  in_symbol_table = False
  for item in symbol_table:
    if item['lexeme'] == lexeme:
      return not in_symbol_table

  return in_symbol_table


def lexeme_match(symbol_table, i, lexeme, type):
  word = rf"\b{lexeme}\b" # f: formatted string; r: regex pattern
  if re.search(word, i):
    in_symbol_table = has_duplicate(lexeme)
    if not in_symbol_table:
      symbol_table.append({ "lexeme": lexeme, "type": type })
    
lines = input_file('files/input.lol')
keywords = input_file('files/keywords.txt') 
symbol_table = []

# print(keywords)
for line in lines:
  for keyword in keywords:
    lexeme_match(symbol_table, line, lexeme=rf"{keyword}", type="keyword")

for symbol in symbol_table:
  print(symbol)