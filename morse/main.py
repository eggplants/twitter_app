#main()
import re
import time
import morse as m
i=0
with open('data.txt',"r") as lines:
    for line in lines:
        i+=1
        print(i)
        try:
            str=m.convdic(line.rstrip())
            #time.sleep(1)
            if re.match(r"[－・]","".join(str[0])):
                print(m.convs(str[0],str[1]))
                #time.sleep(1)
            else:
                print(m.convm(str[0],str[1]))
                #time.sleep(1)
        except IndexError:
                print("<?>")
lines.close()