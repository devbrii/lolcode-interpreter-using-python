arithmetic_operations = ["SUM OF", "DIFF OF", "PRODUKT OF", "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF"]

from lexical_analyzer import *

def variable_declaration1(line):
  try:
    if line[0]['lexeme'] == "I HAS A" and line[1]['type'] == "Variable Identifier" and line[2]['lexeme'] == "ITZ" and line[3]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      return True
  except:
    pass

  return False

def variable_declaration2(line):
  try:
    if line[0]['lexeme'] == "I HAS A" and line[1]['type'] == "Variable Identifier":
      return True
  except:
    pass

  return False

#! VARIABLE ASSIGNMENT
def variable_assignment(line):
  try:
    if line[0]['type'] == "Variable Identifier" and line[1]['lexeme'] == "R" and line[2]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      return True
  except:
    pass

  return False

#! USER INPUT
def user_input(line):
  try:
    if line[0]['lexeme'] == "GIMMEH" and line[1]['type'] == "Variable Identifier":
      return True
  except:
    pass

  return False

#! PRINTING
def printing_variable():
  pass

def printing_string():
  pass

def printing(line):
  try:
    if line[0]['lexeme'] == "VISIBLE":
      return True
  except:
    pass
  return False

def printingExpr(line):
  print("================")
  try:
    operation = ""
    visible_printing = ""
    operator = []
    number = []
    temp_line = line
    if line[0]['lexeme'] == "VISIBLE":
      temp_line = line
      print(temp_line)
      
      counter = 1
      # print(counter)
      # print(len(line))
      while counter < len(temp_line):
        # operators
        if temp_line[counter]['lexeme'] in arithmetic_operations:
          while temp_line[counter]['lexeme'] in arithmetic_operations:
            print(temp_line[counter]['type'])
            if temp_line[counter]['lexeme'] == "SUM OF":
              operator.append("+")
            if temp_line[counter]['lexeme'] == "DIFF OF":
              operator.append("-")
            elif temp_line[counter]['lexeme'] == "PRODUKT OF":
              operator.append("*")
            elif temp_line[counter]['lexeme'] == "QUOSHUNT OF":
              operator.append("/")
            elif temp_line[counter]['lexeme'] == "MOD OF":
              operator.append("%")
              
            counter += 1

          print(temp_line[counter]['lexeme'])
          print(temp_line[counter+1]['lexeme'])


          while temp_line[counter]['type'] == "Variable Identifier" and temp_line[counter+1]['lexeme'] == "AN" or temp_line[counter]['type'] in ["Float", "Integer", "Boolean"] and temp_line[counter+1]['lexeme'] == "AN":
            if temp_line[counter]['type'] == "Variable Identifier":
              for value in symbol_table:
                if value['identifier'] == temp_line[counter]['lexeme']:
                  number.append(value['value'])

            if temp_line[counter]['type'] in ["Float", "Integer", "Boolean"]:
              number.append(temp_line[counter]['lexeme'])

            counter += 2
            expression_flag = True

          if expression_flag:
            if temp_line[counter]['type'] == "Variable Identifier":
              for value in symbol_table:
                if value['identifier'] == temp_line[counter]['lexeme']:
                  number.append(value['value'])

            if temp_line[counter]['type'] in ["Float", "Integer", "Boolean"]:
              number.append(temp_line[counter]['lexeme'])
            counter += 1

          # express in operations
          for index in range(len(number)):
            if index == len(number)-1:
              operation += number[index]
            else:
              operation += number[index]
              operation += operator[index]

          operation = eval(operation)
          visible_printing += str(operation)
        

        if temp_line[counter]['type'] == "String Literal":
          string_literal = temp_line[counter]['lexeme'] 
          string_literal = string_literal.replace("\"", "")
          visible_printing += string_literal
          counter += 1

        print(visible_printing)

      # print(number)
      # print(operator)
  except:
    pass

  return False

# def expression(i):
#   answer = ""
#   try:
#     if line[i][]
#   except:
#     pass
#   pass




#! MAIN
# print(pretty_table)
symbol_table = []

#! will not proceed to semantic analyzer if there are errors from the syntax analyzer
for line in all_table:
  #! VARIABLE DECLARATION
  if variable_declaration1(line):
    has_duplicate = False
    for item in symbol_table:
      try:
        if line[1]['lexeme'] == item['identifier']:
          has_duplicate = True
          item['value'] = line[3]['lexeme']
          break
      except:
        pass
    if not has_duplicate:
      symbol_table.append({ 'identifier': line[1]['lexeme'], 'value': line[3]['lexeme'] })
    continue
  
  if variable_declaration2(line):
    has_duplicate = False
    for item in symbol_table:
      try:
        if line[1]['lexeme'] == item['identifier']:
          has_duplicate = True
          item['value'] = "Untyped"
          break
      except:
        pass

    if not has_duplicate:
      symbol_table.append({ 'identifier': line[1]['lexeme'], 'value': "Untyped" })
    continue

  #! VARIABLE INITIALIZATION  
  if variable_assignment(line):
    has_duplicate = False
    for item in symbol_table:
      try:
        if line[0]['lexeme'] == item['identifier']:
          has_duplicate = True
          break
      except:
        pass

    if has_duplicate == True:
      item['value'] = line[2]['lexeme']
      continue
    else:
      print(f"Error: Variable is not yet defined.")
      break
      
  #! USER INPUT
  if user_input(line):
    variable = input("")

    has_duplicate = False
    for item in symbol_table:
      try:
        if line[1]['lexeme'] == item['identifier']:
          has_duplicate = True
          break
      except:
        pass
    
    if has_duplicate == True:
      item['value'] = variable
      continue
    else:
      print(f"Error: Variable is not yet defined.")
      break

  #! PRINTf
  if printing(line):
    printingExpr(line)
    # pass



pretty_table_semantic = PrettyTable()
pretty_table_semantic.field_names = ["Identifier", "Value"]

print("SYMBOL TABLE")
for line in symbol_table:  
  pretty_table_semantic.add_row([line['identifier'], line['value']])

print(pretty_table_semantic)
