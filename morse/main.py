import re
import morse as m
with open('data.txt') as lines:
    for line in lines:
    str=m.convdic(line.rstrip())
    if re.match(r"[－・]","".join(str[0])):
        print(m.convs(str[0],str[1]))
    else:
        print(m.convm(str[0],str[1]))
    line = f.readline()
f.close()