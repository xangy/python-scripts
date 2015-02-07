'''
 *author:Vishal Kumar
 *description:This script helps to develop options menu for any html page. The options are gathered from any input file.
	Currently, the delimiter is a newline. The options are stored in a list. The list is, then, sorted. Then, the 'option'
	statement is composed and written in the 'output.txt' file.
'''
fout = open("output.txt", "w")
name = raw_input("Enter the name for options:")
line = '<select name="' + name + '">\n\t<option value="default">Select an option</option>\n'
fout.write(line)
inp = raw_input("Enter the file name for list of options:")
fhand = open(inp, "r")
list = list()
for option in fhand :
	option = option.strip()
	list.append(option)
list.sort()
for option in list :
	line = '\t<option value="' + option + '">' + option + '</option>\n'
	fout.write(line)
line = '</select>'
fout.write(line)
fout.close()