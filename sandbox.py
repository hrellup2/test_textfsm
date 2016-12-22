#test
import textfsm


out_file = 'examples/show_version_output.txt'
temp_file = 'examples/show_version_template.txt'

template = open(temp_file,'r')

with open(out_file, 'r') as myfile:
    output=myfile.read().replace('\n', '')


re_table = textfsm.TextFSM(template)
data = re_table.ParseText(output)


print ', '.join(re_table.header)

for row in data:
 print ', '.join(row)
