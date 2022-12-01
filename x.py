arithmetic_operations = ["SUM OF", "DIFF OF", "PRODUKT OF",
                         "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF"]


def expression(line):
    lexeme_index = len(line)
    loop_index = 0
    operators = 0
    operands = 0

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
        print("Yehey")
        return True
    else:
        print("Missing Operand")
        return False


line1 = [{'lexeme': 'answer', 'type': 'Variable Identifier'}, {'lexeme': 'R', 'type': 'R Keyword'}, {'lexeme': 'DIFF OF', 'type': 'Subtraction Operator'}, {'lexeme': 'x', 'type': 'Variable Identifier'}, {'lexeme': 'AN', 'type': 'And Operator'}, {'lexeme': 'y', 'type': 'Variable Identifier'}]

    
expression(line1)
