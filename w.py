import re
rePattern = r'[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
rx = re.compile(rePattern, re.VERBOSE)
print(rx.findall("Some example: Jr. it. was 0.23 between 2.3 and 42.31 seconds"))