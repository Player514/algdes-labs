def print_table_header():
    print("\\medskip")
    print("\\begin{tabular}{lrrrrrr}")
    print("  \\toprule")
    print("  Instance name & $n$ & A & F & M & N & S \\\\")
    print("  \\midrule")


def print_table_footer():
    print("  \\bottomrule")
    print("\\end{tabular}")
    print("\\medskip")


print_table_header()
result_dict = {}
outputFiles = [
    "num_nodes.py_out",
    "alternate.py_out",
    "few.py_out",
    "many.py_out",
    "none.py_out",
    "some.py_out"
]
inputFiles = set()
maxRows = 45
for f in outputFiles:
    result_dict[f] = {}
    with open(f, 'r') as file:
        for line in file:
            lineSplit = line.split('\t')
            if len(lineSplit) == 1:
                lineSplit.append('?')
            fileName, res = [x.strip().rstrip('.txt').lstrip('data/') for x in lineSplit]
            inputFiles.add(fileName)
            result_dict[f][fileName] = res

counter = 0
for file in sorted(inputFiles):
    combined = [file]
    for f in outputFiles:
        if file in result_dict[f]:
            combined.append(result_dict[f][file])
        else:
            combined.append('-')
            # print("Err", file, "missing in", f)
    print('  ' + ' & '.join(combined) + " \\\\")
    counter += 1
    if counter % maxRows == 0:
        print_table_footer()
        print_table_header()
print_table_footer()
