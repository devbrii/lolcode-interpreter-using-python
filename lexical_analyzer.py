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


def specific_keyword(keyword, line, symbol_table, lexeme_type):
    if keyword in line:  # keyword is an operator
        symbol_table.append({"lexeme": keyword, "type": lexeme_type})
        # del line_split[line_index: line_index+len(keyword_split)]
        line = line.replace(keyword, "", 1)
    
    return line


lines = input_file('test_cases/sample.lol')

symbol_table = []

# sorted in descending order per length of string
# Why? when keyword is "YR" and first line is "IM IN YR LOOP", it will remove "YR" in the list
# better to filter all the longer words first
all_keywords = [
    ["IM OUTTA YR", "Loop"],
    ["I HAS A", "Variable Declaration"],
    ["QUOSHUNT OF", "Division Operator"],
    ["SMALLR OF", "Smaller Of"],
    ["BOTH SAEM", "Equal Operator"],
    ["DIFFRINT", "Not Equal Operator"],
    ["IS NOW A", "Typecasting"],
    ["IM IN YR", "Loop Start"],
    ["BIGGR OF", "Bigger Of"],
    ["KTHXBYE", "End of Code"],
    ["I HAS A", "Variable Declaration"],
    ["VISIBLE", "Print Statement"],
    ["DIFF OF", "Subtraction Operator"],
    ["NUMBRAR", "Float Type"],
    ["SMOOSH", "String Concatenation"],
    ["GIMMEH", "Input"],
    ["O RLY?", "If Statement"],
    ["YA RLY", "True Expression"],
    ["NO WAI", "False Expression"],
    ["OMGWTF", "Default Case Comparison"],
    ["NERFIN", "Decrement By One"],
    ["SUM OF", "Addition Operator"],
    ["MOD OF", "Modulo Operator"],
    ["WON OF", "XOR Operation"],
    ["ANY OF", "Or Operator Infinite Args"],
    ["ALL OF", "And Operator Infinite Args"],
    ["MEBBE", "If-Else Optional"],
    ["UPPIN", "Increment By One"],
    ["NUMBR", "Integer Type"],
    ["TROOF", "Boolean Type"],
    ["MAEK", "Typecast"],
    ["WTF?", "Switch Start"],
    ["WILE", "Loop Execution Continues If True"],
    ["GTFO", "Break Statement"],
    ["NOOB", "Untyped Data Type"],
    ["FAIL", "False Value"],
    ["HAI", "Start of Code"],
    ["ITZ", "Assignment Operator"],
    ["OIC", "End of If Statement"],
    ["OMG", "Switch Case Start"],
    ["TIL", "Loop Execution Continues One More Time If False"],
    ["WIN", "True Value"],
    ["HAI", "Start of code"],
    ["AN", "And Operator"],
    ["YR", "YR Loop Keyword"],
    ["IT", "IT Keyword"],
    ["R", "R Keyword"],
    ["A", "A Keyword"]
]

obtw_flag = 0
for line in lines:
    if "BTW" in line:  # remove all succeeding lines
        symbol_table.append({"lexeme": "BTW", "type": "Comment"})

        splitted_list = line.split()
        index = splitted_list.index("BTW")
        splitted_list = splitted_list[0:index] # remove all string starting from BTW to the end of the line
        line = ' '.join([str(elem) for elem in splitted_list]) # convert back to string

    # returns a list of matches if there are multiple strings
    string_matches = re.findall(r'"(.+?)"', line)
    for match in string_matches:
        symbol_table.append(
            {"lexeme": f"\"{match}\"", "type": "String Literal"})
        line = line.replace(match, "", 1)

    for item in all_keywords:
        occurences = line.count(item[0])
        for occurence in range(occurences):
            line = specific_keyword(item[0], line, symbol_table, item[1])

    #     line_index = 0
    #     keyword_split = keyword.split()

    #     while line_index <= len(line_split)-len(keyword_split):
    #         if (keyword_split == line_split[line_index: line_index+len(keyword_split)]):
    #             search_keywords(symbol_table, line_split)
    #             # TODO: word TLDR does not accept commands after it
    #             if keyword == "OBTW":  # remove all succeeding lines
    #                 symbol_table.append({"lexeme": keyword, "type": "Comment"})
    #                 del line_split[line_index: len(line_split)]
    #                 obtw_flag = 1
    #                 break

    #         line_index += 1

    #     if obtw_flag == 1:
    #         break

    # if obtw_flag == 1:
    #     # ! assume that user puts TLDR in the first part
    #     if "TLDR" not in line_split:
    #         line_split = []
    #         continue
    #     else:
    #         if "TLDR" == line_split[0]:
    #             tldr = line_split.pop(0)
    #             tldr_remaining = line_split[0:]
    #             print("TLDR", tldr_remaining)
    #             symbol_table.append({"lexeme": tldr, "type": "Comment"})

    #             for keyword in all_keywords:
    #                 tldr_index = 0
    #                 keyword_split = keyword.split()
    #                 while tldr_index <= len(tldr_remaining)-len(keyword_split):
    #                     if (keyword_split == tldr_remaining[tldr_index: tldr_index+len(keyword_split)]):
    #                         search_keywords(symbol_table, tldr_remaining)
    #                     tldr_index += 1
    #             obtw_flag = 0

    # line_split = ' '.join(line_split)  # group into a string again per line

    # TODO: turn into function
    # returns a list of matches if there are integers in each line
    int_matches = re.findall(r'(?<!\.)\b[0-9]+\b(?!\.)', line)
    for match in int_matches:
        symbol_table.append({"lexeme": match, "type": "Integer"})
        line = line.replace(match, "", 1)

    # returns a list of matches if there are multiple floats in each line
    int_matches = re.findall(r'(\b\d+?\.\d+\b)', line)
    for match in int_matches:
        symbol_table.append({"lexeme": match, "type": "Float"})
        line = line.replace(match, "", 1)

    for line in line.split():
        if line != "\"\"":
            symbol_table.append(
                {"lexeme": line, "type": "Variable Identifier"})

    print(f"AFTER: {line}")

# output file
pretty_table = PrettyTable()
pretty_table.field_names = ["Lexeme", "Type"]

#! at the end of a file, OBTW has no TLDR partner
if obtw_flag == 1:
    symbol_table = []


for symbol in symbol_table:
    print(symbol)
    pretty_table.add_row([symbol['lexeme'], symbol['type']])

print(pretty_table)
print(len(symbol_table))
