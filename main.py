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

lib = {
    'OPERATOR': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'KEYWORDS': ['int', 'float', 'real', 'bool', 'True', 'False', 'if', 'else', 'then', 'endif', 'endelse',
                 'while', 'whileend', 'do', 'enddo', 'for', 'endfor', 'STDinput', 'STDoutput', 'and', 'or', 'not'],
    'SEPARATORS': ['()', '(', ')', '{', '}', '[', ']', ',', '.', ':', ';']
}


if __name__ == "__main__":
    test2 = []
    with open('testFile.txt') as file:
        line = file.readline()
        while line:
            line = re.sub("!.*?!", "", line)  # Removes Comment blocks
            test = re.findall(
                r"[\d+\.\d+]+|[\w']+|[.,?;]+|[\(\)\{\}\[\]]+|[+-/!=<>%]", line)
            test2.append(test)
            # print(test)
            line = file.readline()
    print("%-15s %-15s %s" % ('TOKEN', " ", 'LEXEMES'))
    print(' ')
    identify_type(test2)







