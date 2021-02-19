import re

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
                print(f"INT: {i}")
            elif isfloat(i):
                print(f"REAL: {i}")
            elif i in lib['OPERATOR']:
                print(f"OPERATOR: {i}")
            elif i in lib['KEYWORDS']:
                print(f"KEYWORDS: {i}")
            elif i in lib['SEPARATORS']:
                print(f"SEPARATORS: {i}")
            else:
                print(f"IDENTIFIER: {i}")

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
    identify_type(test2)







