from prettytable import PrettyTable
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import re
import os
os.system('cls')

# ---------------------------------------------------------
win = tk.Tk()
win.geometry("1000x400")
win.title("LOLCode Interpreter")
# ---------------------------------------------------------
lolcode_frame = tk.Frame(win, width=250)
lolcode_frame.grid(row=0, column=0, padx=10, pady=5, ipadx=0, ipady=0)

lexsym_frame = Frame(win, width=400)
lexsym_frame.grid(row=0, column=2, padx=10, pady=5, ipadx=0, ipady=0)

# lexeme_frame = Frame(lexsym_frame, width=200, highlightbackground="grey", highlightthickness=3)
# lexeme_frame.grid(row=0, column=1, padx=20, pady=20, ipadx=20, ipady=20)

# symtab_frame = Frame(lexsym_frame, width=220, highlightbackground="grey", highlightthickness=3)
# symtab_frame.grid(row=0, column=2, padx=20, pady=20, ipadx=20, ipady=20)

# lolcode_frame2 = tk.Frame(lolcode_frame, width=250, highlightbackground="grey", highlightthickness=3)
# lolcode_frame2.grid(row=1, column=0, padx=10, pady=5, ipadx=0, ipady=0)

text_path = tk.Entry(lolcode_frame, width=56)
text_path.grid(row=0, column=0)

icon = PhotoImage(file="folder.png")

btn_get_path = tk.Button(lolcode_frame, image=icon, width=12, height=12, relief=FLAT, command=lambda: set_path(text_path))
btn_get_path.grid(row=0, column=1)

my_lolcode = tk.Text(win, width=51, height=10, font=("Helvetica", 10))
my_lolcode.grid(row=1, column=0, padx=20, pady=10)

# title_frame2 = tk.Text()

# class Line:
#     def __init__(self):
#         self._lines = []
    
#     def get_lines(self):
#         print("getter called")
#         return self._lines

#     def set_lines(self, x):
#         print("setter called")
#         self._lines = x

def set_path(entry_field):
    path = fd.askopenfilename(initialdir="C:/Users/vincent/Desktop/cmsc124-project/", title="Open File")
    entry_field.delete(0, tk.END)
    entry_field.insert(0, path)

    path = open(path, 'r')
    stuff = path.read()

    my_lolcode.insert(END, stuff)

    input_file(path.name)

    path.close()


# read file
def input_file(file_name):
    file_in = open(file_name, "r")

    lines = []

    for line in file_in:
        line = line.strip()  # removes \n
        lines.append(line)

    # linexx = Line()
    # linexx.set_lines(lines)

    process(lines)


def specific_keyword(keyword, line, symbol_table, lexeme_type):
    if keyword in line:  # keyword is an operator
        symbol_table.append({"lexeme": keyword, "type": lexeme_type})
        # del line_split[line_index: line_index+len(keyword_split)]
        line = line.replace(keyword, "", 1)
    
    return line


def process(lines):
    all_table = []

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
        line_split = line.split()
        lexemes_table = []
        
        while line_split != []:
            # for BTW
            try:
                # print("LINE SPLIT: ", line_split)
                index = line_split.index('BTW')
                lexemes_table.append({"lexeme": "BTW", "type": "Single Line Comment"})
                line_split = line_split[:index]
                continue
                # print("LINE SPLIT: ", line_split)
            except:
                pass
            
            continue_flag = 0
            for keyword in all_keywords:
                keyword_split = keyword[0].split()

                if keyword_split == line_split[:len(keyword_split)]:
                    # print("PASS")
                    lexemes_table.append({"lexeme": keyword[0], "type": keyword[1]})

                    line_split = line_split[len(keyword_split):]
                    continue_flag = 1
                    
                    break

            if continue_flag == 1:
                continue

            # string literal
            try:
                if "\"" in line_split[0]:
                    # re.match(r'(?<!\.)\b[0-9]+\b(?!\.)', line_split)
                    line_split = ' '.join(line_split)  # group into a string again
                
                    string_matches = re.findall(r'"(.+?)"', line_split)
                    for match in string_matches:
                        lexemes_table.append({"lexeme": f"\"{match}\"", "type": "String Literal"})
                        line_split = line_split.replace(match, "")
                    line_split = line_split.split()
                    break
            except:
                pass

            
            try:
                if re.match(r'(?<!\.)\b[0-9]+\b(?!\.)', line_split[0]):
                    lexemes_table.append({"lexeme": line_split[0], "type": "Integer"})
                    line_split = line_split[1:]
                    continue
            except:
                pass

            try:
                if re.findall(r'(\b\d+?\.\d+\b)', line_split[0]):
                    lexemes_table.append({"lexeme": line_split[0], "type": "Float"})
                    line_split = line_split[1:]
                    # continue
            except:
                pass

            try:
                lexemes_table.append({"lexeme": line_split[0], "type": "Variable Identifier"})
                line_split = line_split[1:]
                
            except:
                pass

        all_table.append(lexemes_table)


        # print(f"AFTER: {line}")

    # output file
    pretty_table = PrettyTable()
    pretty_table.field_names = ["Lexeme", "Type"]

    #! at the end of a file, OBTW has no TLDR partner
    # if obtw_flag == 1:
    #     lexemes_table = []


    # for lexemes in lexemes_table:
        # pretty_table.add_row([lexemes['lexeme'], lexemes['type']])

    # print(pretty_table)
    # print(len(lexemes_table))


    for line in all_table:
        print(line)
        for lexeme in line:
            pretty_table.add_row([lexeme['lexeme'], lexeme['type']])

    print(pretty_table)
    # print(len(symbol_table))

def main():

    # process()

    win.mainloop()

main()