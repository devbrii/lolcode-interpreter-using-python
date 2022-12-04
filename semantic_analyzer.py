from syntax_analyzer import *

print(pretty_table)
symbol_table = []

#! will not proceed to semantic analyzer if there are errors from the syntax analyzer
if not cannot_proceed:
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


pretty_table_semantic = PrettyTable()
pretty_table_semantic.field_names = ["Identifier", "Value"]

print("SYMBOL TABLE")
for line in symbol_table:  
  pretty_table_semantic.add_row([line['identifier'], line['value']])

print(pretty_table_semantic)
