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

def penalty(f, t="*", blosum=[], indices={}):    
    return blosum[indices[f]][indices[t]]

def parse_blosum(location="data/BLOSUM62.txt"): 
    regex = re.compile("(^\w |\* )")
    all_lines = open(location, "r").readlines()
    indices = all_lines[6].strip().split('  ')
    as_dict = {v: i for i, v in enumerate(indices)}
    blosum = all_lines[7:]
    blosum = list(map(lambda line: list(map(lambda lll: int(lll), filter(lambda ll: ll != '', line.strip()[regex.search(line).lastindex+1:].split(' ')))), blosum))
    return blosum, as_dict

def find_difference(i, j, x, y, cache, blosum, indices, gap):
    if i == 0 and j == 0: 
        return 0 

    if i == 0 or j == 0: 
        return gap  # What is the delta value here? 

    mismatch_penalty = penalty(x[i], y[j], blosum, indices)

    case_1 = mismatch_penalty + find_difference(i-1, j-1, x, y, cache, blosum, indices, gap) \
        if cache[i-1][j-1] == None else cache[i-1][j-1]
    cache[i-1][j-1] = case_1

    case_2 = gap + find_difference(i-1, j, x, y, cache, blosum, indices, gap) \
        if cache[i-1][j] == None else cache[i-1][j]
    cache[i-1][j] = case_2

    case_3 = gap + find_difference(i, j-1, x, y, cache, blosum, indices, gap) \
        if cache[i][j-1] == None else cache[i][j-1]
    cache[i][j-1] = case_3

    print(case_1, case_2, case_3)
    minimum = min([case_1, case_2, case_3])
    print(minimum)
    return minimum

def find_differences(input, blosum, indices, gap):
    differences = {}
    cache = None
    for i in reversed(range(0, len(input))):
        for j in reversed(range(i+1, len(input))):
            first_string = input[i][1]
            second_string = input[j][1]

            cache_dimension = max(len(first_string), len(second_string))
            cache = [[None] * cache_dimension] * cache_dimension
            difference = find_difference(len(first_string)-1, len(second_string)-1, first_string, second_string, cache, blosum, indices, gap)
            
            first_name = input[i][0]
            second_name = input[j][0]
            combined = f"{first_name}--{second_name}"
            resulting_string = "Missing\nMissing" # TODO: Implement finding actual difference string
            differences[combined] = (difference, resulting_string)
    
    return differences

def print_differences(differences):
    for key, value in differences.items():
        print(f"{key}: {value[0]}\n{value[1]}")

gap = -4
data = parse_input(sys.stdin)
blosum, indices = parse_blosum("BLOSUM62.txt")
differences = find_differences(data, blosum, indices, gap)
print_differences(differences)