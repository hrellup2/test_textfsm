#test
import textfsm


out_file = 'examples/show_clock_out.txt'
temp_file = 'examples/show_clock_temp.txt'

template = open(temp_file,'r')

with open(out_file, 'r') as myfile:
    output=myfile.read().replace('\n', '')


print output
print template
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(output)


print ', '.join(re_table.header)

print data
for row in data:
 print ', '.join(row)
