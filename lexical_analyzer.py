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

def lexeme_match(symbol_table, i, lexeme, type):
  if re.search(rf"\b{lexeme}\b", i): # f: formatted string; r: regex pattern
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


# print(lexemes)