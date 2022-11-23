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

def search_keywords(symbol_table, delimiter, operators, general, bool_list, line_split):
  # TODO: turn into function
  if keyword in delimiter:  # keyword is an operator
      symbol_table.append({"lexeme": keyword, "type": "Delimiter"})
      del line_split[line_index : line_index+len(keyword_split)]
      
  if keyword in operators:  # keyword is an operator
      symbol_table.append({"lexeme": keyword, "type": "Operator"})
      del line_split[line_index : line_index+len(keyword_split)]

  if keyword in general:  # all general keywords
      symbol_table.append({"lexeme": keyword, "type": "Keyword"})
      del line_split[line_index : line_index+len(keyword_split)]

  if keyword in bool_list:  # all boolean
      symbol_table.append({"lexeme": keyword, "type": "Booelan"})
      del line_split[line_index : line_index+len(keyword_split)]

  if keyword == "BTW": # remove all succeeding lines
      symbol_table.append({"lexeme": keyword, "type": "Comment"})
      del line_split[line_index : len(line_split)]


lines = input_file('test_cases/sample.lol')

all_keywords = input_file('interpreter_files/all_keywords.txt')
general = input_file('interpreter_files/keywords.txt')
operators = input_file('interpreter_files/operators.txt')
bool_list = input_file('interpreter_files/bool.txt')
delimiter = input_file('interpreter_files/delimiter.txt')
symbol_table = []

obtw_flag = 0
for line in lines:
    # splits the line per word
    line_split = line.split()

    # for all keywords
    for keyword in all_keywords:
        line_index = 0
        keyword_split = keyword.split()
        
        while line_index <= len(line_split)-len(keyword_split):
            if (keyword_split == line_split[line_index : line_index+len(keyword_split)]):
                search_keywords(symbol_table, delimiter, operators, general, bool_list, line_split)
                # TODO: word TLDR does not accept commands after it 
                if keyword == "OBTW": # remove all succeeding lines
                    symbol_table.append({"lexeme": keyword, "type": "Comment"})
                    del line_split[line_index : len(line_split)]
                    obtw_flag = 1
                    break

            line_index += 1

        if obtw_flag == 1:
            break
    
    if obtw_flag == 1:
        # ! assume that user puts TLDR in the first part
        if "TLDR" not in line_split:
            line_split = []
            continue
        else:
            if "TLDR" == line_split[0]:
                tldr = line_split.pop(0)
                tldr_remaining = line_split[0:]
                print("TLDR", tldr_remaining)
                symbol_table.append({"lexeme": tldr, "type": "Comment"})

                for keyword in all_keywords:
                    tldr_index = 0
                    keyword_split = keyword.split()
                    while tldr_index <= len(tldr_remaining)-len(keyword_split):
                        if (keyword_split == tldr_remaining[tldr_index : tldr_index+len(keyword_split)]):
                            search_keywords(symbol_table, delimiter, operators, general, bool_list, tldr_remaining)
                        tldr_index += 1  
                obtw_flag = 0



    line_split = ' '.join(line_split) # group into a string again per line

    # TODO: turn into function
    string_matches = re.findall(r'"(.+?)"', line_split) # returns a list of matches if there are multiple strings   
    for match in string_matches:
        symbol_table.append({"lexeme": f"\"{match}\"", "type": "String Literal"})
        line_split = line_split.replace(match, "")

    int_matches = re.findall(r'(?<!\.)\b[0-9]+\b(?!\.)', line_split) # returns a list of matches if there are integers in each line   
    for match in int_matches:
        symbol_table.append({"lexeme": match, "type": "Integer"})
        line_split = line_split.replace(match, "")

    int_matches = re.findall(r'(\b\d+?\.\d+\b)', line_split) # returns a list of matches if there are multiple floats in each line  
    for match in int_matches:
        symbol_table.append({"lexeme": match, "type": "Float"})
        line_split = line_split.replace(match, "")

    for line in line_split.split():
        if line != "":
            symbol_table.append({"lexeme": line, "type": "Variable Identifier"})

    print(f"AFTER: {line_split}")
    
# output file
pretty_table = PrettyTable()
pretty_table.field_names = ["Lexeme", "Type"]

#! at the end of a file, OBTW has no TLDR partner
if obtw_flag == 1:
  symbol_table = []

for symbol in symbol_table:
    pretty_table.add_row([symbol['lexeme'], symbol['type']])

print(pretty_table)
print(len(symbol_table))