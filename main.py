import re

lib = {
    'OPERATOR': ['+', '-', '*', '/', '=', '>', '<', '%'],
    'KEYWORDS': ['int', 'float', 'bool', 'True', 'False', 'if', 'else', 'then', 'endif', 'endelse',
                 'while', 'whileend', 'do', 'enddo', 'for', 'endfor', 'STDinput', 'STDoutput', 'and', 'or', 'not'],
    'SEPARATORS': ['(', ')', '{', '}', '[', ']', ',', '.', ':', ';']
}


if __name__ == "__main__":
    with open('testFile.txt') as file:
        line = file.readline()
        while line:
            test = re.findall(
                r"[\w']+|[.,!?;]+|[\(\)\{\}\[\]]+|[+-=/<>%]", line)
            print(test)
            line = file.readline()
