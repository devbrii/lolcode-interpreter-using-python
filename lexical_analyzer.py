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


def specific_keyword(keyword_split, new_line, symbol_table, lexeme_type):
  if keyword_split == new_line[0:len(keyword_split)]:
    symbol_table.append({"lexeme": keyword, "type": lexeme_type})
    # del line_split[line_index: line_index+len(keyword_split)]
    # line = line.replace(keyword, "", 1)
    new_line = new_line[len(keyword):]

  return new_line


all_table = []

lines = input_file('test_cases/sample.lol')

# sorted in descending order per length of string
# Why? when keyword is "YR" and first line is "IM IN YR LOOP", it will remove "YR" in the list
# better to filter all the longer words first
all_keywords = [
    ["IM OUTTA YR", "Loop"],
    ["I HAS A", "Variable Declaration"],
    ["QUOSHUNT OF", "Division Operator"],
    ["PRODUKT OF", "Division Operator"],
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
    ["MKAY", "Mkay Keyword"],
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
string_flag = 0

for line in lines:
  line_split = line.split()
  lexemes_table = []

  # while every line is not an empty list
  while line_split:
    print(line_split)
    #! OBTW
    try:
      if line_split.index('OBTW') == 0:
        del line_split[0]
        lexemes_table.append({"lexeme": "OBTW", "type": "Multiline Comment Start"})
        obtw_flag = 1
        continue
    except:
      pass

    #! BTW
    try:
      if line_split.index('BTW') == 0:
        index = 0
        lexemes_table.append(
            {"lexeme": "BTW", "type": "Single Line Comment"})
        line_split = []
        continue
      # print("LINE SPLIT: ", line_split)
    except:
      pass

    #! ALl Keywrods
    continue_flag = 0
    for keyword in all_keywords:
      keyword_split = keyword[0].split()

      if keyword_split == line_split[:len(keyword_split)]:
        lexemes_table.append({"lexeme": keyword[0], "type": keyword[1]})

        line_split = line_split[len(keyword_split):]
        continue_flag = 1

        break

    if continue_flag == 1:
        continue

    # string literal
    try:
        if "\"" == line_split[0][0]:
          lexemes_table.append({"lexeme": "\"", "type": "String Delimiter"})
          del line_split[0]
          string_flag = 1
          # print("LINE 0 0", line_split[0][0])
          # line_split = ' '.join(line_split)  # group into a string again

          # string_matches = re.findall(r'"(.+?)"', line_split)
          # for match in string_matches:
          #     lexemes_table.append({"lexeme": f"\"{match}\"", "type": "String Literal"})
          #     line_split = line_split.replace(match, "")
          # line_split = line_split.split()
          break
    except:
        pass

    string_literal = ""
    while string_flag == 1:
      # lexemes_table.append({"lexeme": "\"", "type": "String Delimiter"})
      try:
        if line_split[0][-1] == "\"":
          lexemes_table.append({"lexeme": string_literal, "type": "String Literal"})
          lexemes_table.append({"lexeme": "\"", "type": "String Delimiter"})
        else:
          string_literal = string_literal.join(line_split[0])  # group into a string again
        del line_split[0]
      except:
        pass




    try:
        if re.match(r'(?<!\.)\b[0-9]+\b(?!\.)', line_split[0]):
            lexemes_table.append({"lexeme": line_split[0], "type": "Integer"})
            del line_split[0]
            continue
    except:
        pass

    try:
        if re.findall(r'(\b\d+?\.\d+\b)', line_split[0]):
            lexemes_table.append(
                {"lexeme": line_split[0], "type": "Float"})
            del line_split[0]
            continue
    except:
        pass

    try:
      if obtw_flag == 1:
        if line_split[0] == "TLDR":
          del line_split[0]
          obtw_flag = 0
          lexemes_table.append({"lexeme": "TLDR", "type": "Multiline Comment End"})
        else:
          line_split = []
        continue

    except:
      pass


    try:
        if re.match(r'^([a-z])[a-z0-9_]*', line_split[0]):
            lexemes_table.append(
                {"lexeme": line_split[0], "type": "Variable Identifier"})
            del line_split[0]
            continue
    except:
        pass


    try:
        lexemes_table.append({"lexeme": line_split[0], "type": "Undetermined"})
        del line_split[0]
    except:
        pass

  all_table.append(lexemes_table)


# output file
pretty_table = PrettyTable()
pretty_table.field_names = ["Lexeme", "Type"]

for line in all_table:
    for lexeme in line:
        pretty_table.add_row([lexeme['lexeme'], lexeme['type']])

print(pretty_table)

# for line in all_table:
#   print(line)