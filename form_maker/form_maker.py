import json

def main(outName, JSON_path, to_url):
	with open(JSON_path, 'r') as read_in:
		in_dict = json.load(read_in)

	strOut = "<!DOCTYPE html><html><head><title>"
	strOut += in_dict['name']
	strOut += "</title>"
	strOut += "<script src=\"jquery-3.4.1.min.js\"></script>"
	strOut += "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js\"></script>"
	strOut += "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>"
	strOut += "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css\">"

	strOut += "</head><body><div class=\"container\"><div class=\"col-sm-12\">"
	strOut += "<div class=\"jumbotron\"> <h1>"
	strOut += in_dict['name']
	strOut += "</h1> <p class=\"lead\">"
	strOut += in_dict['description']
	strOut += "</p> <hr class=\"my-4\"></div>"

	strOut += "<form>"

	for i in in_dict['args']:
		strOut += getInput(i);
		strOut += "<br />"

	strOut += "<input onclick = \"submit()\" class=\"btn btn-primary btn-lg btn-block\" type=\"submit\">"

	strOut += "</form>"
	strOut += "</div></div><script>"

	strOut += '''
	function submit() {
		// POST DATAS
		$.post({
		  url: \''''+to_url+'''\',
		  data: {
		  	'''
	for i in in_dict['args']:
		strOut += getPoster(i);
	strOut += '''
		  },
		  success: function(dt) {
			window.location.href = "/";
		  }
		});
	}
	'''



	strOut += "</script></body></html>"

	f = open(outName, 'w+')
	f.write(strOut)
	f.close()


def getInput(dic_in):
	name = dic_in['name']
	ret_val = "<h3>"
	ret_val += name
	ret_val += ":</h3>"
	ret_val += "<input class=\"form-control\" type=\"";
	if dic_in['type'] == 'float' or dic_in['type'] == 'int':
		ret_val += 'number'
	elif dic_in['type'] == 'string':
		ret_val += 'text'

	ret_val += "\" id=\""+name.replace(" ", "-")+"\" name=\""
	ret_val += dic_in['name']
	ret_val += "\">"
	return(ret_val)

def getPoster(dic_in):
	name = dic_in['name']
	ret_val= "\'"+name+"\': $(\'#"+name.replace(" ", "-")+"\').val(),"
	return ret_val
	#$('#username').val();
main('out.html', 'test.json', '/assets')
