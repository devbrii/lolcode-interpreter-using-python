# import re
# import os
# os.system('cls')
# from prettytable import PrettyTable

# # read file
# def input_file(file_name):
#   with open(file_name) as file_in:
#     lines = []
#     for line in file_in:
#       line = line.strip() # removes \n
#       lines.append(line)
#   return lines

# lines = input_file('test_cases/sample.lol')
# new_lines = []
# keywords = input_file('interpreter_files/keywords.txt') 
# operators = input_file('interpreter_files/operators.txt') 
# symbol_table = []

# for line in lines:
#     for word in keywords:
#         if (line.find(word)) != -1:
#           new_lines.append(word)
#           line.replace(word, "")
#           symbol_table.append({"lexeme": word, "type": "keyword" })

# pretty_table = PrettyTable()
# pretty_table.field_names = ["Lexeme", "Type"]

# for symbol in symbol_table:
#   pretty_table.add_row([symbol['lexeme'], symbol['type']])

# print()
# print(pretty_table)

