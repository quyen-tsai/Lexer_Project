import re

def print_format(data, output):
    print("%-15s %-15s %s" % (data, "=", output))

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def identify_type(test2):
    for items in test2:
        for i in items:
            if i.isdigit():
                print("%-15s %-15s %s" % ('INT', "=", i))
            elif isfloat(i):
                print("%-15s %-15s %s" % ('REAL', "=", i))
            elif i in lib['OPERATOR']:
                print("%-15s %-15s %s" % ('OPERATOR', "=", i))
            elif i in lib['KEYWORDS']:
                print("%-15s %-15s %s" % ('KEYWORDS', "=", i))
            elif i in lib['SEPARATORS']:
                print("%-15s %-15s %s" % ('SEPARATOR', "=", i))
            else:
                print("%-15s %-15s %s" % ('IDENTIFIER', "=", i))

lib2 = {
    'l':'_abcdefghijklmnopqrstuvwxyz$',
    'digs': '#0123456789.',
    'ct': ['(', ')', '{', '}', '[', ']', ',', ':', ';'],
    'op': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'sp': [' ']
}

lib = {
    'OPERATOR': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'KEYWORDS': ['int', 'float', 'real', 'bool', 'True', 'False', 'if', 'else', 'then', 'endif', 'endelse',
                 'while', 'whileend', 'do', 'enddo', 'for', 'endfor', 'STDinput', 'STDoutput', 'and', 'or', 'not'],
    'SEPARATORS': ['()', '(', ')', '{', '}', '[', ']', ',', ':', ';']
}

if __name__ == "__main__":
    test2 = []
    with open('testFile.txt') as file:
        line = file.readline()
        temp = ''
        print("%-15s %-15s %s" % ('TOKEN:', " ", 'LEXEMES:'))
        print(' ')
        while line:
            line = re.sub("!.*?!", "", line)  # Removes Comment blocks
            state = 1
            for char in line:
                if char == '\n':
                    char = ' '
                if state == 1:
                    if char.lower() in lib2['l']:
                        state = 2
                        temp += char
                    elif char in lib2['digs']:
                        state = 4
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        if temp.isdigit() and char != ' ':
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '':
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '' and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        if char in lib['OPERATOR']:
                            print("%-15s %-15s %s" % ('OPERATOR', "=", char))
                        elif char in lib['SEPARATORS']:
                            print("%-15s %-15s %s" % ('SEPARATOR', "=", char))
                        temp = ''
                elif state == 2:
                    if char in lib2['l']:
                        state = 2
                        temp += char
                    elif char in lib2['digs']:
                        state = 2
                        temp += char
                    elif char in lib2['sp']:
                        state = 3
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '':
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 3
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '' and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        if char in lib['OPERATOR']:
                            print("%-15s %-15s %s" % ('OPERATOR', "=", char))
                        elif char in lib['SEPARATORS']:
                            print("%-15s %-15s %s" % ('SEPARATOR', "=", char))
                        temp = ''
                elif state == 3:
                    if char in lib2['l']:
                        state = 1
                        temp += char
                    elif char in lib2['digs']:
                        state = 1
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp == '':
                            state = 1
                        elif temp != ' ' and temp != '':
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
                        temp += char
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '' and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        if char in lib['OPERATOR']:
                            print("%-15s %-15s %s" % ('OPERATOR', "=", char))
                        elif char in lib['SEPARATORS']:
                            print("%-15s %-15s %s" % ('SEPARATOR', "=", char))
                        temp = ''
                elif state == 4:
                    if char in lib2['l']:
                        state = 5
                        temp += char
                    if char in lib2['digs']:
                        temp += char
                    elif char in lib2['sp']:
                        state = 5
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '':
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 5
                        if char in lib['OPERATOR']:
                            print("%-15s %-15s %s" % ('OPERATOR', "=", char))
                        elif char in lib['SEPARATORS']:
                            print("%-15s %-15s %s" % ('SEPARATOR', "=", char))
                        if temp.isdigit() and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp) and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS'] and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '' and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))

                        temp = ''
                elif state == 5:
                    if char in lib2['l']:
                        state = 1
                        temp += char
                    elif char in lib2['digs']:
                        state = 1
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '':
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
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
                        temp = ''
                elif state == 6:
                    if char in lib2['l']:
                        state = 1
                        temp += char
                    elif char in lib2['digs']:
                        state = 1
                        temp += char
                    elif char in lib2['sp']:
                        state = 1
                        if temp.isdigit():
                            print("%-15s %-15s %s" % ('INT', "=", temp))
                        elif isfloat(temp):
                            print("%-15s %-15s %s" % ('REAL', "=", temp))
                        elif temp in lib['KEYWORDS']:
                            print("%-15s %-15s %s" % ('KEYWORDS', "=", temp))
                        elif temp != ' ' and temp != '':
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        temp = ''
                    elif char in lib2['ct'] or char in lib2['op']:
                        state = 1
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
                        elif temp != ' ' and temp != '' and char not in lib2['op']:
                            print("%-15s %-15s %s" % ('IDENTIFIER', "=", temp))
                        temp = ''
            line = file.readline()