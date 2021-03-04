import re
import sys



def isfloat(value): #check to see if variable is a float type
    try:
        float(value)
        return True
    except ValueError:
        return False

""" 
check for punctuation or operators. If there is punctuation, decide whether or not
the operator or punc. would be included in the temp string to be output to screen
"""
def identify_typeCT(char, temp):
    if char in lib['OPERATOR']:
        print("%-15s %-15s %s" % ('OPERATOR', "=", char))
    elif char in lib['SEPARATORS']:
        print("%-15s %-15s %s" % ('SEPARATOR', "=", char))
    if temp.isdigit() and char not in lib2['ct'] and temp != ' ' and temp != '' and char not in lib2['op']:
        print("%-15s %-15s %s" % ('INT', "=", temp))
    elif isfloat(temp) and char not in lib2['ct'] and temp != ' ' and temp != '' and char not in lib2['op']:
        print("%-15s %-15s %s" % ('REAL', "=", temp))
    elif temp in lib['KEYWORDS'] and char not in lib2['ct'] and temp != ' ' and temp != '' and char not in lib2['op']:
        print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
    elif temp !=  ' ' and temp != '' and char not in lib2['op']:
        print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))

#Outputs the type and type name a space has been found
def identify_typeSP(temp):
    if temp.isdigit():
        print("%-15s %-15s %s" % ('INT', "=", temp))
    elif isfloat(temp):
        print("%-15s %-15s %s" % ('REAL', "=", temp))
    elif temp in lib['KEYWORDS']:
        print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
    elif temp != ' ' and temp != '':
        print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))

#Library to check for individual characters to see if valid
lib2 = {
    'l':'_abcdefghijklmnopqrstuvwxyz$',
    'digs': '#0123456789.',
    'ct': ['(', ')', '{', '}', '[', ']', ',', ':', ';'],
    'op': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'sp': [' ']
}

#Library to reference operator, Keywords and separators
lib = {
    'OPERATOR': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'KEYWORDS': ['int', 'float', 'real', 'bool', 'True', 'False', 'if', 'else', 'then', 'endif', 'endelse',
                 'while', 'whileend', 'do', 'enddo', 'for', 'endfor', 'STDinput', 'STDoutput', 'and', 'or', 'not'],
    'SEPARATORS': ['()', '(', ')', '{', '}', '[', ']', ',', ':', ';']
}

if __name__ == "__main__":
    filename = input("Please enter File path:")
    orig_stdout = sys.stdout
    f = open('output.txt', 'w')
    sys.stdout = f
    with open(filename) as file:
        line = file.readline()
        temp = ''
        print("%-15s %-15s %s" % ('TOKEN:', " ", 'LEXEMES:'))
        print(' ')
        while line: #Main loop to analyze file
            line = re.sub("!.*?!", "", line)  # Removes Comment blocks
            state = 1
            for char in line: #secondary loop to analyze each character
                if char == '\n':
                    char = ' '
                if state == 1: #Initial state
                    if char.lower() in lib2['l']:
                        state = 2
                        temp += char
                    elif char in lib2['digs']:
                        state = 4
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        identify_typeSP(temp)
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
                        identify_typeCT(char, temp)
                        temp = ''
                elif state == 2: #State to identify  Identifier
                    if char in lib2['l']:
                        state = 2
                        temp += char
                    elif char in lib2['digs']:
                        state = 2
                        temp += char
                    elif char in lib2['sp']:
                        state = 3
                        identify_typeSP(temp)
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 3
                        identify_typeCT(char, temp)
                        temp = ''
                elif state == 3: #State signify ending of identifier
                    if char in lib2['l']:
                        state = 1
                        temp += char
                    elif char in lib2['digs']:
                        state = 1
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        identify_typeSP(temp)
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
                        temp += char
                        identify_typeCT(char, temp)
                        temp = ''
                elif state == 4: # state for begin of digits
                    if char in lib2['l']:
                        state = 5
                        temp += char
                    if char in lib2['digs']:
                        temp += char
                    elif char in lib2['sp']:
                        state = 5
                        identify_typeSP(temp)
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 5
                        identify_typeCT(char, temp)
                        temp = ''
                elif state == 5: #state signify ending of digits
                    if char in lib2['l']:
                        state = 1
                        temp += char
                    elif char in lib2['digs']:
                        state = 1
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        identify_typeSP(temp)
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
                        identify_typeCT(char, temp)
                        temp = ''
                elif state == 6: #state to identify general punctuation and operators
                    if char in lib2['l']:
                        state = 1
                        temp += char
                    elif char in lib2['digs']:
                        state = 1
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        identify_typeSP(temp)
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
                        identify_typeCT(char, temp)
                        temp = ''
            line = file.readline()
    sys.stdout = orig_stdout
    f.close()
    file.close()
