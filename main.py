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
    if temp.isdigit() or char.isdigit() and char not in lib2['ct'] and temp != ' ' and temp != '' and char not in lib2['op']:
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
    'KEYWORDS': ['int', 'float', 'real', 'boolean', 'True', 'False', 'true','false', 'if', 'else', 'then', 'endif', 'endelse',
                 'while', 'whileend', 'do', 'enddo', 'for', 'endfor', 'STDinput', 'STDoutput', 'and', 'or', 'not'],
    'SEPARATORS': ['()', '(', ')', '{', '}', '[', ']', ',', ':', ';']
}

lib5 = {
    'Type':['int', 'float', 'boolean', 'real', 'double']
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
    f = open('Lexical_analysis.txt', 'w')
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
            o = copy(x, i)
            if o != 0:
                i = o
                t.append(vec[hodl:i])
                hodl = i
    return t


def statement(a_switch, x, i, x_switch, line):
    if x[i] == 'int' or x[i] == 'float' or x[i] == 'bool':
        print(f"Token: Keyword      Lexemes: {x[i]}")
        print("<Statement> -> <Declarative>")
        Declarative(x[i])
        return a_switch, x_switch
    elif a_switch == 0:
        if x[i] in lib3['id']:
            print(f"Token: Identifier     Lexemes: {x[i]}")
        print("<Statement> -> <Assign>")
        assign(x, i, a_switch, x_switch,line)
        a_switch += 1
        return a_switch, x_switch
    elif x[i] == '=':
        print(f"Token:Separator     Lexemes: {x[i]}")
        return a_switch, x_switch
    else:
        a_switch, x_switch = assign(x, i, a_switch, x_switch,line)
        return a_switch, x_switch


def assign(x, i, a_switch, x_switch,line):
    temp = 0
    if a_switch == 0:
        print("<Assign> -> <Identifier> = <Expression>")
    else:
        temp = expression(i, x, x_switch, a_switch,line)
    return int(a_switch), int(temp)

def Declarative(x):
    print("<Declarative> -> <Type> <ID>")
    Type(x)

def Type(x):
    if x == 'int':
        print("<Type> -> int")
        return
    elif x == 'bool':
        print("<Type> -> bool")
        return
    elif x == 'float':
        print("<Type> -> float")
        return

def copy(x, o):
    i = o
    sums = ''
    while i < len(vec):
        sums += str(vec[i])
        if sums == x:
            return i + 1
        i += 1
    return 0


def expression_prime(x):
    if x == '+':
        print("<Expression Prime> -> +<Term><Expression Prime>")
    elif x == '-':
        print("<Expression Prime> -> -<Term><Expression Prime>")
    elif x == ';':
        print("<Expression Prime> -> E")
    return 0


def term(x):
    print("<Term> -> <Factor><Term Prime>")
    if x != '+' and x != '-' and x != '*' and x != '/' and x != ';':
        factor(x)
    elif x == '*' or x == '/' or x == '+' or x == '-':
        term_prime(x)
    return 0


def term_prime(x):
    if x == "*":
        print("<Term prime> -> *<Factor><Term prime>")
    elif x == "/":
        print("<Term prime> -> /<Factor><Term prime>")
    elif x in lib['OPERATOR'] or x in lib['SEPARATORS']:
        print("<Term Prime> -> E")


def factor(x):
    if x in lib3['id']:
        print("<Factor> -> <Identifier>")
    elif x.isdigit():
        print("<Factor> -> <Num>")
    elif x == '(' or x == ')':
        print("<Factor> -> ( <Expression> )")
    return 0


def ID(x):
    return 0


def expression(i, x, x_switch, a_switch, line):
    if x[i] in lib3['id'] and a_switch != 0:
        print(f"Token: Identifier     Lexemes: {x[i]}")
    elif x[i] in lib3['Key']:
        print(f"Token: Keyword     Lexemes: {x[i]}")
    elif x[i] in lib3['OP']:
        print(f"Token: Operator     Lexemes: {x[i]}")
    elif x[i] in lib3['SE']:
        print(f"Token: Separator     Lexemes: {x[i]}")
    elif x[i] in lib3['INT']:
        print(f"Token: Digit integer     Lexemes: {x[i]}")
    elif x[i] in lib3['FLOAT']:
        print(f"Token: Digit Float     Lexemes: {x[i]}")
    if x[i] == '=':
        return x_switch
    elif x_switch == 0 and x[i] != '(' and x[i] != ')' and x[i] != '+' and x[i] != '-' and x[i] != '*' and x[i] != '/' and x[i] != ';' and x[i] not in lib3['SE']:
        x_switch += 1
        print("<Expression> -> <Term><Expression Prime>")
        term(x[i])
        return x_switch
    else:
        if x[i].isdigit():
            term(x[i])
        if x[i] == '+' or x[i] == '-':
            if i == len(x) -1:
                print(f"Syntax Error, no Identifier following operator on line {line}")
                return -1
            elif x[i+1] not in lib3['id']  and i < len(x):
                if x[i+1] == '(':
                    if ')' not in x:
                        print(f"Missing closing Parentheses on line {line}")
                        return -1
                    else:
                        count = 0
                        for k in range(x.index('('),x.index(')')):
                            if x[k] in lib3['id']:
                                count += 1
                        if count == 0:
                            print(f"Uncomputable code on line {line}")
                            return -1
                    term_prime(x[i])
                    expression_prime(x[i])
                    x_switch = 0
                elif x[i+1].isdigit():
                    term(x[i])
                else:
                    print(f"Syntax error, cannot compute code on line {line}")
                    return -1
            else:
                term_prime(x[i])
                expression_prime(x[i])
        elif x[i] == ';':
            if i == len(x) -1:
                term_prime(x[i])
                expression_prime(x[i])
            else:
                print(f"Syntax Error on line {line}")
                return -1
        elif x[i] == '*' or x[i] == '/':
            if i == len(x) -1:
                print(f"Syntax Error, no Identifier following operator on line {line}")
                return -1
            elif x[i+1] not in lib3['id'] and i < len(x):
                print(f"Syntax error, cannot compute code on line {line}")
                return -1
            term(x[i])
        else:
            term(x[i])
    return x_switch


def syntaxAnalysis2(vec3):
    line = 1
    orig_stdout = sys.stdout
    f2 = open('Syntax_analysis.txt', 'w')
    sys.stdout = f2
    for x in vec3:
        if not x:
            line += 1
        x_switch = 0
        a_switch = 0
        for i in range(len(x)):
            if ('int' in x or 'float' in x or 'bool' in x) and ('=' in x):
                if len(x) < 2:
                    print(f"Syntax Error on line {line}")
                    return None
                a_switch, x_switch = statement(a_switch, x, i, x_switch,line)
                if x_switch == -1:
                    return None
                print(" ")
            elif ('int' in x or 'float' in x or 'bool' in x) and ('=' not in x):
                if len(x) < 2:
                    print(f"Syntax Error on line {line}")
                    return None
                a_switch, x_switch = statement(a_switch, x, i, x_switch, line)
                if x_switch == -1:
                    return None
                print(" ")
            elif '=' in x:
                if len(x) < 3:
                    print(f"Syntax Error on line {line}: missing assignment for variable {x[i]}")
                    return None
                a_switch, x_switch = statement(a_switch, x, i, x_switch,line)
                if x_switch == -1:
                    return None
                print(" ")
            else:
                if(len(x) < 1):
                    print(f"Syntax Error on line {line}: un-executable code")
                    return None
                if x[i] == '(':
                    if ')' not in x:
                        print(f"Missing closing Parentheses on line {line}")
                        return None
                    elif len(x) <3:
                        print(f"Syntax Error: un-executable expression on line {line}")
                        return None
                    else:
                        count = 0
                        for k in x:
                            if k in lib3['id']:
                                count+=1
                        if count <= 1:
                            print(f"Uncomputable code on line {line}")
                            return None
                        a_switch = 1
                        x_switch = 0
                        x_switch = expression(i, x, x_switch, a_switch,line)
                        if x_switch == -1:
                            return None
                        print(" ")
                else:
                    a_switch = 1
                    x_switch = expression(i, x, x_switch, a_switch,line)
                    if x_switch == -1:
                        return None
                    print(" ")

        line +=1
    print("Code Compile Successfully")
    sys.stdout = orig_stdout
    f2.close()

lib4 = {}
memory_add = 5000
def simp_table(vec3,memory_add):
    orig_stdout = sys.stdout
    f2 = open('Syntax_analysis.txt', 'w')
    sys.stdout = f2
    line = 1
    ide = ""
    clear = True
    for x in vec3:
        if not x:
            continue
        elif len(x) < 1:
            print(f"Error on line {line}, invalid syntax")
            return False
        elif x[0] == '{' or x[0] == '}'or x[0] == 'if'or x[0] == 'else'or x[0] == 'endif':
            continue
        if x[0] in lib3['Key'] and x[0] in lib5['Type']:
            if len(x) < 2:
                print(f"Missing identifier after data type {x[0]} on line {line}")
                return False
            ide = x[0]
            count = 0
            for i in range(len(x)):
                t = x[i]
                if x[i] == ';' and i+1 == len(x):
                    break
                if (x[i] in lib['SEPARATORS'] or x[i] in lib['OPERATOR']) and i+1 == len(x):
                    print(f'Syntax error on line {line} no identifier following {x[i]}')
                    return False
                elif (x[i] in lib['SEPARATORS'] or x[i] in lib['OPERATOR']) and x[i+1] not in lib3['id'] :
                    if x[i].isdigit:
                        pass
                    else:
                        print(f'Syntax error on line {line} no identifier following {x[i]}')
                        return False
            for i in x:
                if i.isdigit():
                    pass;
                elif i == '=':
                    for j in range(x.index(i), len(x)):
                        if x[j] not in lib4 and x[j] not in lib['OPERATOR'] and x[j] not in lib['SEPARATORS'] and not x[j].isdigit():
                            print(f"Syntax error on line {line}, '{x[j]}' was not declared in this scope")
                            return False
                elif i in lib3['Key'] and count > 0:
                    print(f"Syntax error on line {line}!")
                    return False
                elif i == ide:
                    pass
                elif i not in lib['OPERATOR'] and i not in lib['SEPARATORS'] and i not in lib4:
                    lib4[i] = ide
                elif i in lib4:
                    print(f"{i} already exist on line {line}! Can't initialize same identifier twice!")
                    return False
                count+=1
        elif x[0] not in lib3['Key']:
            for i in x:
                if i not in lib4 and i not in lib3['SE'] and i not in lib3['OP'] and not i.isdigit():
                    if i == 'true' or i == 'false' or i == 'True' or i == 'False':
                        pass
                    else:
                        print(f"{i} was not declared in this scope on line {line}")
                        return False

        line+=1
    sys.stdout = orig_stdout
    f2.close()
    print("Symbol Table")
    print("%-15s %-15s %s" % ('Identifier', "MemoryLocation", 'Type'))
    for x in lib4:
        print("%-15s %-15s %s" % (x, str(memory_add), lib4[x]))
        memory_add += 1
    return True

parsingTable1 = ['+','-','id','$']
parsingTable2 = [
    ['>','<','<','>'],
    ['>','>','<','>'],
    ['>','>','ER','>'],
    ['<','<','<','ER'],
]


def syntaxAnalysis3(vec3):
    line = 1
    #orig_stdout = sys.stdout
    #f2 = open('Syntax_analysis.txt', 'w')
    #sys.stdout = f2
    terminal = ['E', 'EPrime', 'T', 'TPrime', 'F', 'S', 'A', 'D', 'Ty']
    for x in vec3:
        if not x:
            line += 1
        x.append('$')
        i = 0
        stack = []
        stack.insert(0, '$')
        while not(stack[0] == '$' and x[i] == '$'):
            if(stack[0] in lib3['id']):
                t = parsingTable1.index('id')
            else:
                t = parsingTable1.index(stack[0])
            if not x:
                pass
            elif(x[i] in lib3['id']):
                s = parsingTable1.index('id')
            elif (x[i] == '+'):
                s = parsingTable1.index('+')
            elif (x[i] == '-'):
                s = parsingTable1.index('-')
            elif (x[i] == '$') or (x[i] in terminal):
                s = parsingTable1.index('$')
            entry = parsingTable2[t][s]

            if(entry == 'ER'):
                print(f'Error with Syntax{line}')
                return None
            elif(entry == '>'):
                checkRule = ""
                while True:
                    char = stack.pop(0)
                    if char == '<':
                        break
                    else:
                        checkRule += char
                syntaxCheck(stack, checkRule)
            else:
                if '<' not in stack:
                    stack.insert(len(stack) - 2, entry)
                    stack.insert(0, x[i])
                else:
                    stack.insert(0, entry)
                    stack.insert(0, x[i])
                i += 1

def syntaxCheck(stack, checkRule):
    pass

if __name__ == "__main__":
    #filename = input("Please enter File path:")
    filename = 'testFile.txt'
    lexar(filename)
    vec3 = vec_mod()
    print(lib3)
    print(vec3)
    clear = simp_table(vec3,memory_add)

    if(clear):
        syntaxAnalysis3(vec3)



