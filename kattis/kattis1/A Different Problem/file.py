import sys
import re

for line in sys.stdin:
    group = re.search('(\d*) (\d*)',line)
    num1 = float(group.group(1))
    num2 = float(group.group(2))
    print(int(abs(num1-num2)))