import json

def main():
	with open("test.json", 'r') as read_in:
		in_dict = json.load(read_in)

	print(in_dict['name'])

	strOut = "<!DOCTYPE html><html><head><title>"
	strOut += in_dict['name']
	strOut += "</title>"
	strOut += "<script src=\"jquery-3.4.1.min.js\"></script>"
	strOut += "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js\"></script>"

	strOut += "</head><body>"
	strOut += "<h1>"
	strOut += in_dict['name']
	strOut += "</h1>"

	strOut += "<form>"

	for i in in_dict['args']:
		strOut += getInput(i);
		strOut += "<br />"

	strOut += "</form>"
	strOut += "</body></html>"

	f = open("out.html", 'w+')
	f.write(strOut)
	f.close()


def getInput(dic_in):
	ret_val = dic_in['name']
	ret_val += "<input type=\"";
	if dic_in['type'] == 'float' or dic_in['type'] == 'int':
		ret_val += 'number'
	elif dic_in['type'] == 'string':
		ret_val += 'text'

	ret_val += "\" id=\"\" class=\"\" name=\""
	ret_val += dic_in['name']
	ret_val += "\">"
	return(ret_val)

main()
