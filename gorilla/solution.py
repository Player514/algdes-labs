import sys
import re

def parse_input(input):
    data = []
    name = None
    string = ""
    read = False
    for i, line in enumerate(input):
        line = line.strip()
        if '>' in line: 
            if (i != 0): 
                data.append((name, string))
            name = line[1:].split(' ')[0]
            string = ""
            continue

        string += line

    data.append((name, string))
    return data

def print_data(data):
    for t in data: 
        print(f"{t[0]:>15}, {t[1]}")

char_index = { 'A': 0, 'R': 1, 'N': 2, 'D': 3, 'C': 4, 'Q': 5, 'E': 6, 'G': 7, \
               'H': 8, 'I': 9, 'L':10, 'K':11, 'M':12, 'F':13, 'P':14, 'S':15, \
               'T':16, 'W':17, 'Y':18, 'V':19, 'B':20, 'Z':21, 'X':22, '*':23 }
def penalty(f, t="*", blosum=[]):    
    first_i = char_index[f]
    second_i = char_index[t]
    return blosum[first_i][second_i]

def parse_blosum(location="data/BLOSUM62.txt"): 
    regex = re.compile("(^\w |\* )")
    blosum = open(location, "r").readlines()[7:]
    blosum = list(map(lambda line: list(map(lambda lll: int(lll), filter(lambda ll: ll != '', line.strip()[regex.search(line).lastindex+1:].split(' ')))), blosum))
    return blosum

def find_differences(input):
    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            first = input[i]
            second = input[j]

            print(first, '---', second)

data = parse_input(sys.stdin)
blosum = parse_blosum("data/BLOSUM62.txt")
find_differences(data)