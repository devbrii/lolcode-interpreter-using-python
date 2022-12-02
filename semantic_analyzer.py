from syntax_analyzer import *

print(pretty_table)
symbol_table = []


def find_duplicate(lexeme_type, duplicate, lexeme_type2):
  try:
    if lexeme_type == duplicate:
      item['value'] = lexeme_type2
      return True
  except:
    pass

  return False

has_duplicate = False
#! will not proceed to semantic analyzer if there are errors from the syntax analyzer
if not cannot_proceed:
  for line in all_table:
    #! VARIABLE DECLARATION
    if variable_declaration1(line):
      if line[3]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
        for item in symbol_table:
          has_duplicate = find_duplicate(line[1]['lexeme'], item['identifier'], line[3]['lexeme'])
        if not has_duplicate:
          symbol_table.append({ 'identifier': line[1]['lexeme'], 'value': line[3]['lexeme'] })
      continue
    
    if variable_declaration2(line):
      print(line)
      for item in symbol_table:
        has_duplicate = find_duplicate(line[1]['lexeme'], item['identifier'], "Untyped")
      if not has_duplicate:
        symbol_table.append({ 'identifier': line[1]['lexeme'], 'value': "Untyped" })
      continue

    #! VARIABLE INITIALIZATION  
    # if variable_initialize(line): return True


    # #! USER INPUT
    # if user_input(line): return True
    # if user_input_error(line): return False

pretty_table_semantic = PrettyTable()
pretty_table_semantic.field_names = ["Identifier", "Value"]

for line in symbol_table:  
  pretty_table_semantic.add_row([line['identifier'], line['value']])

print(pretty_table_semantic)
