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

def find_difference(i, j, x, y, cache, blosum, gap):

    #TODO: This never terminates... Why? 

    if i == 0: 
        return gap # What is the delta value here? 
    if j == 0: 
        return gap # What is the delta value here? 

    mismatch_penalty = cache[i][j] if cache[i][j] != None else penalty(x[i], y[j], blosum)
    cache[i][j] = mismatch_penalty
    case_1 = mismatch_penalty + find_difference(i-1, j-1, x, y, cache, blosum, gap)
    case_2 = gap + find_difference(i-1, j, x, y, cache, blosum, gap)
    case_3 = gap + find_difference(i, j-1, x, y, cache, blosum, gap)

    minimum = min([case_1, case_2, case_3])
    return minimum

def find_differences(input, blosum, gap):
    differences = {}
    cache = None
    for i in reversed(range(0, len(input))):
        for j in reversed(range(i+1, len(input))):
            first_string = input[i][1]
            second_string = input[j][1]
            first_string = first_string + ('*' * (len(second_string)-len(first_string))) if len(second_string) > len(first_string) else first_string
            second_string = second_string + ('*' * (len(first_string)-len(second_string))) if len(first_string) > len(second_string) else second_string

            cache = [[None] * len(first_string)] * len(second_string)
            difference = find_difference(len(first_string)-1, len(second_string)-1, first_string, second_string, cache, blosum, gap)
            
            first_name = input[i][0]
            second_name = input[j][0]
            combined = f"{first_name}--{second_name}"
            resulting_string = "" # TODO: Implement finding actual difference string
            differences[combined] = (difference, resulting_string)
    
    return differences

def print_differences(differences):
    for key, value in differences.items():
        print(f"{key}: {value[0]}\n{value[1]}")

gap = -4
data = parse_input(sys.stdin)
blosum = parse_blosum("data/BLOSUM62.txt")
differences = find_differences(data, blosum, gap)
print_differences(differences)