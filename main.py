import re

lib = {
    'OPERATOR': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'KEYWORDS': ['int', 'float', 'bool', 'True', 'False', 'if', 'else', 'then', 'endif', 'endelse',
                 'while', 'whileend', 'do', 'enddo', 'for', 'endfor', 'STDinput', 'STDoutput', 'and', 'or', 'not'],
    'SEPARATORS': ['()', '(', ')', '{', '}', '[', ']', ',', '.', ':', ';']
}

test2 = []
if __name__ == "__main__":
    with open('testFile.txt') as file:
        line = file.readline()
        while line:
            test = re.findall(
                r"[\w']+|[.,!?;]+|[\(\)\{\}\[\]]+|[+-=/<>%]", line)
            test2.append(test)
            print(test)
            line = file.readline()

print(test2)
for items in test2:
    for i in items:
        if i.isdigit():
            print(f"INT: {i}")
        elif i in lib['OPERATOR']:
            print(f"OPERATOR: {i}")
        elif i in lib['KEYWORDS']:
            print(f"KEYWORDS: {i}")
        elif i in lib['SEPARATORS']:
            print(f"SEPARATORS: {i}")
        else:
            print(f"IDENTIFIER: {i}")


