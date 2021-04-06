import re
import sys


def isfloat(value):  # check to see if variable is a float type
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
    if temp.isdigit() and char not in lib2['ct'] and temp != ' ' and temp != '' and char not in lib2['op']:
        vec.append(temp)
        print("%-15s %-15s %s" % ('INT', "=", temp))
        if temp not in lib3['INT']:
            lib3['INT'].append(temp)
    elif isfloat(temp) and char not in lib2['ct'] and temp != ' ' and temp != '' and char not in lib2['op']:
        vec.append(temp)
        if temp not in lib3['FLOAT']:
            lib3['FLOAT'].append(temp)
        print("%-15s %-15s %s" % ('REAL', "=", temp))
    elif temp in lib['KEYWORDS'] and char not in lib2['ct'] and temp != ' ' and temp != '' and char not in lib2['op']:
        vec.append(temp)
        if temp not in lib3['Key']:
            lib3['Key'].append(temp)
        print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
    elif temp in lib['KEYWORDS'] and temp != ' ' and temp != '':
        vec.append(temp)
        if temp not in lib3['Key']:
            lib3['Key'].append(temp)
        print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
    elif temp != ' ' and temp != '' and temp not in lib['OPERATOR'] and temp not in lib['SEPARATORS']:
        vec.append(temp)
        if temp not in lib3['id']:
            lib3['id'].append(temp)
        print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
    if char in lib['OPERATOR']:
        vec.append(char)
        if char not in lib3['OP']:
            lib3['OP'].append(char)
        print("%-15s %-15s %s" % ('OPERATOR', "=", char))
    elif char in lib['SEPARATORS']:
        vec.append(char)
        if char not in lib3['SE']:
            lib3['SE'].append(char)
        print("%-15s %-15s %s" % ('SEPARATOR', "=", char))


# Outputs the type and type name a space has been found


def identify_typeSP(temp):
    if temp.isdigit():
        vec.append(temp)
        print("%-15s %-15s %s" % ('INT', "=", temp))
        if temp not in lib3['INT']:
            lib3['INT'].append(temp)
    elif isfloat(temp):
        vec.append(temp)
        if temp not in lib3['FLOAT']:
            lib3['FLOAT'].append(temp)
        print("%-15s %-15s %s" % ('REAL', "=", temp))
    elif temp in lib['KEYWORDS']:
        vec.append(temp)
        print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
        if temp not in lib3['Key']:
            lib3['Key'].append(temp)
    elif temp != ' ' and temp != '' and temp not in lib['OPERATOR'] and temp not in lib['SEPARATORS']:
        vec.append(temp)
        print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
        if temp not in lib3['id']:
            lib3['id'].append(temp)


# Library to check for individual characters to see if valid
lib2 = {
    'l': '_abcdefghijklmnopqrstuvwxyz$',
    'digs': '#0123456789.',
    'ct': ['(', ')', '{', '}', '[', ']', ',', ':', ';'],
    'op': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'sp': [' ']
}

# Library to reference operator, Keywords and separators
lib = {
    'OPERATOR': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'KEYWORDS': ['int', 'float', 'real', 'bool', 'True', 'False', 'if', 'else', 'then', 'endif', 'endelse',
                 'while', 'whileend', 'do', 'enddo', 'for', 'endfor', 'STDinput', 'STDoutput', 'and', 'or', 'not'],
    'SEPARATORS': ['()', '(', ')', '{', '}', '[', ']', ',', ':', ';']
}

lib3 = {
    'id': [],
    'Key': [],
    'OP': [],
    'SE': [],
    'INT': [],
    'FLOAT': []
}

vec = []


def lexar(filename):
    orig_stdout = sys.stdout
    f = open('output.txt', 'w')
    sys.stdout = f
    with open(filename) as file:
        line = file.readline()
        temp = ''
        print("%-15s %-15s %s" % ('TOKEN:', " ", 'LEXEMES:'))
        print(' ')
        while line:  # Main loop to analyze file
            line = re.sub("!.*?!", "", line)  # Removes Comment blocks
            line = line.replace('\n', ' ')
            line = line.replace('\t', ' ')
            state = 1
            vec2.append(str(line))
            for char in line:  # secondary loop to analyze each character
                if state == 1:  # Initial state
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
                elif state == 2:  # State to identify  Identifier
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
                elif state == 3:  # State signify ending of identifier
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
                elif state == 4:  # state for begin of digits
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
                elif state == 5:  # state signify ending of digits
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
                elif state == 6:  # state to identify general punctuation and operators
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
            identify_typeSP(temp)
            line = file.readline()
    sys.stdout = orig_stdout
    f.close()
    file.close()


vec2 = []
vec3 = []


def syntaxAnalysis(vec):
    for x in vec:
        if x == ' ':
            continue
        if x in lib3['id']:
            print(f"Token: Identifier     Lexemes: {x}")
        elif x in lib3['Key']:
            print(f"Token: Keyword     Lexemes: {x}")
        elif x in lib3['OP']:
            print(f"Token: Operator     Lexemes: {x}")
        elif x in lib3['SE']:
            print(f"Token: Separator     Lexemes: {x}")
        elif x in lib3['INT']:
            print(f"Token: Digit integer     Lexemes: {x}")
        elif x in lib3['FLOAT']:
            print(f"Token: Digit Float     Lexemes: {x}")


def vec_mod():
    t = []
    o = 0
    i = 0
    hodl = 0
    for x in vec2:
        x = str(x).replace(' ', '')
        if x == '' or x == ' ':
            t.append([])
        elif o == 0:
            o = copy(x, i)
            if o != 0:
                i = o
                t.append(vec[0:i])
                hodl = i
        else:
            o = copy(x,i)
            if o != 0:
                i = o
                t.append(vec[hodl:i])
                hodl = i
    return t



def copy(x, o):
    i = o
    sums = ''
    while i < len(vec):
        sums += str(vec[i])
        if sums == x:
            return i + 1
        i += 1
    return 0



if __name__ == "__main__":
    # filename = input("Please enter File path:")
    filename = 'testFile.txt'
    lexar(filename)
    vec3 = vec_mod()
    print (vec3)
    syntaxAnalysis(vec)
