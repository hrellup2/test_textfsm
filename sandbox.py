#test
import textfsm

template = open('examples/show_chassis_routing-engine_template.txt','r')

with open('examples/show_chassis_routing-engine_output.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(data)
