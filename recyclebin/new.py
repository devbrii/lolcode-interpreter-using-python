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

obtw_flag = 1

for line in lines:
    # splits the line per word
    line_split = line.split()

    # for all keywords
    for keyword in all_keywords:
        line_index = 0
        keyword_split = keyword.split()

        while line_index <= len(line_split)-len(keyword_split):
            if (keyword_split == line_split[line_index:line_index+len(keyword_split)] or obtw_flag == 1):

                if keyword in operators:  # keyword is an operator
                    symbol_table.append(
                        {"lexeme": keyword, "type": "Operator"})
                    del line_split[line_index : line_index+len(keyword_split)]
                if keyword in general:  # all general keywords
                    symbol_table.append(
                        {"lexeme": keyword, "type": "Keyword"})
                    del line_split[line_index : line_index+len(keyword_split)]
                if keyword == "BTW": # remove all succeeding lines
                    symbol_table.append({"lexeme": keyword, "type": "Comment"})
                    del line_split[line_index : len(line_split)]
                if keyword == "OBTW": # remove all succeeding lines
                    symbol_table.append({"lexeme": keyword, "type": "Comment"})
                    del line_split[line_index : len(line_split)]
                    obtw_flag = 1

            # if obtw_flag == 1:
            #     if keyword == "TLDR":
            #         del line_split[line_index : line_index+len(keyword_split)]
            #     else:

                    

            line_index += 1

    print(line_split)

    # if

# output file
pretty_table = PrettyTable()
pretty_table.field_names = ["Lexeme", "Type"]

for symbol in symbol_table:
    pretty_table.add_row([symbol['lexeme'], symbol['type']])

print(pretty_table)
# print(symbol)

# for symbol in symbol_table:
#   print(symbol)
