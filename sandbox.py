#test
import textfsm



template = open('examples/show_clock_temp.txt','r')

with open('examples/show_clock_out.txt', 'r') as myfile:
    output=myfile.read().replace('\n', '')


print output
print template
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(output)


print ', '.join(re_table.header)

print data
for row in data:
 print ', '.join(row)
