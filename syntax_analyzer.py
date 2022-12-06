from lexical_analyzer import *


def loop(line):
  pass


def typecast(line):
  if len(line) < 4:
    print("Syntax Error: Missing an operand.")
    return False
  
  if line[1]["type"] not in ["Float", "Integer", "Variable Identifier", "Boolean", "True Value", "False Value", "Untyped Data Type"]:
    print("Syntax Error: Expecting a literal")
    return False
  else:
    if line[2]["lexeme"] != "A":
      print("Syntax Error: ")
      return False
    else:
      if line[3]["lexeme"] not in ["NUMBR", "TROOF", "NUMBAR"]:
        print("Expecting a valid data type to typecast")
        return False

  return True
      
#! VARIABLE DECLARATION
def expression(line):
    lexeme_index = len(line)
    loop_index = 0
    operators = 0
    operands = 0

    if line[0]['lexeme'] == "MAEK":
      return typecast(line)

    while loop_index < lexeme_index:
        print(loop_index)
        print(line[loop_index]['lexeme'])

        if line[loop_index]['lexeme'] in arithmetic_operations:
            if loop_index +1 == lexeme_index:
                operands+1
                loop_index+=1
                continue

            if line[loop_index+1]['lexeme'] not in arithmetic_operations and line[loop_index+1]['type'] not in ["FLOAT", "INTEGER", "Variable Identifier"]:
                print("Missing an operand")
                return False
            else:
                operators += 1

        if line[loop_index]['type'] in ["FLOAT", "INTEGER", "Variable Identifier"] and operators>0:
            if loop_index +1 == lexeme_index:
                operands+1
                loop_index+=1
                continue

            if line[loop_index+1]['lexeme'] != "AN":
                print("Expression syntax error")
                return False
            else:
                operands += 1

        if line[loop_index]['lexeme'] == "AN":
            if loop_index +1 == lexeme_index:
                operands+1
                loop_index+=1
                continue

            if line[loop_index+1]['lexeme'] in arithmetic_operations:
                operators += 1
            elif line[loop_index+1]['type'] in ["FLOAT", "INTEGER", "Variable Identifier"]:
                operands += 1
            else:
                print("Expression syntax error")
                return False
        loop_index += 1
    if operands - 1 == operators:
        print("YEHEY")
        return True
    else:
        print("Missing Operand")
        return False

def variable_declaration1(line):
  try:
    if line[0]['lexeme'] == "I HAS A" and line[1]['type'] == "Variable Identifier" and line[2]['lexeme'] == "ITZ" and line[3]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      return True
  except:
    pass

  return False

def variable_declaration1_error(line):
  try:
    if line[0]['lexeme'] == "I HAS A" and line[1]['type'] == "Variable Identifier" and line[2]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      print("Syntax Error: Missing \"ITZ Keyword\"")
      return True
  except:
    pass

  return False

def variable_declaration1_error2(line):
  try:
    if line[0]['lexeme'] == "I HAS A" and line[1]['type'] == "Variable Identifier" and line[2]['lexeme'] == "ITZ":
      print("Syntax Error: Missing literal, variable, or expression")
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

def variable_declaration_error(line):
  try:
    if line[0]['lexeme'] == "I HAS A":
      print("Syntax Error: Missing variable identifier")
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

def variable_assignment_error1(line):
  try:
    if line[0]['type'] == "Variable Identifier" and line[1]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      print("Syntax Error: Missing 'R' keyword")
      return True
  except:
    pass

  return False

def variable_assignment_error2(line):
  try:
    if line[0]['type'] == "Variable Identifier" and line[1]['lexeme'] == "R":
      print("Syntax Error: Missing literal, variable, or expression")
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

def user_input_error(line):
  try:
    if line[0]['lexeme'] == "GIMMEH":
      print("Syntax Error: Missing variable identifier")
      return True
  except:
    pass

  return False

def statements(line):
  #! VARIABLE DECLARATION
  # if len(line) >0:
  #   if line[0] in arithmetic_operations+["MAEK", "SMOOSH"]:
  #     if expression(line): return True
  #     elif not expression(line): return False
  #   if line[0] == "IM":
  #     print() 
    if variable_declaration1(line): return True
    if variable_declaration1_error(line): return False
    if variable_declaration1_error2(line): return False
    if variable_declaration2(line): return True
    if variable_declaration_error(line): return False

    #! VARIABLE INITIALIZATION  
    if variable_assignment(line): return True
    if variable_assignment_error1(line): return False
    if variable_assignment_error2(line): return False

    #! USER INPUT
    if user_input(line): return True
    if user_input_error(line): return False



arithmetic_operations = ["SUM OF", "DIFF OF", "PRODUKT OF", "QUOSHUNT OF" ,"MOD OF", "BIGGR OF", "SMALLR OF"]
hai_flag = False
bye_flag = False
error_flag = False
cannot_proceed = False

line_index = 0
for line in all_table:
  lexeme_index = 0
  line_index += 1
  
  for lexeme in line:
    if lexeme['lexeme'] == "HAI":
      hai_flag = not hai_flag

      if len(line) == 2:
        if line[lexeme_index+1]['type'] not in ["Single Line Comment", "Integer", "Float"]:
          print("Error")

    if lexeme['lexeme'] == "KTHXBYE":
      bye_flag = not bye_flag

    lexeme_index += 1

  # show errors
  if statements(line) == False:
    error_flag = True
    break
  
  if statements(line) == True:
    continue
  

if error_flag == False and not (hai_flag and bye_flag):
  print("Syntax Error: Missing HAI or KTHXBYE")
  cannot_proceed = True

if error_flag == True:
  cannot_proceed = True

print("Line", line_index)

    # pretty_table.add_row([lexeme['lexeme'], lexeme['type']])

# for line in all_table:
#   # if variable_declaration1(line):
#   print(line)