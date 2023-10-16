from flask import Flask, request

app = Flask('lab03')

@app.route('/hello', methods=['GET','POST'])
def my_form():
	doc = ''
	if(request.method == 'GET'):
		value = request.args.get('param_get')
	
		doc += '<!doctype html>'
		doc += '<html lang="en">'
		doc += '<head>'
		doc += '</head>'
		doc += '<body>'
		doc += '<h1>result with get method</h1>'
		doc += '<hr>'
		doc += 'hello, ' + value + '!'
		doc += '</body>'
		doc += '</html>'
	
	if(request.method == 'POST'):
		value = request.form['param_post']
	
		doc += '<!doctype html>'
		doc += '<html lang="en">'
		doc += '<head>'
		doc += '</head>'
		doc += '<body>'
		doc += '<h1>result with post method</h1>'
		doc += '<hr>'
		doc += 'hello, ' + value + '!'
		doc += '</body>'
		doc += '</html>'
	
	return doc
	
@app.route('/calc', methods=['GET','POST'])
def my_calc():
	doc = ''
	doc += '<!doctype html>'
	doc += '<html lang="en">'
	doc += '<head>'
	doc += '</head>'
	doc += '<body>'
	if(request.method == 'GET'):
		a = int(request.args.get('paramA'))
		b = int(request.args.get('paramB'))
		doc += '<h1>calc result</h1><hr>'
		
		if request.args.get('add'):
			res = a + b
			doc += '<p>' + str(a) + ' + ' + str(b) + ' = ' +  str(res) + '</p>'
		elif request.args.get('subtruct'):
			res = a - b
			doc += '<p>' + str(a) + ' - ' + str(b) + ' = ' +  str(res) + '</p>'
		elif request.args.get('multiply'):
			res = a * b
			doc += '<p>' + str(a) + ' * ' + str(b) + ' = ' +  str(res) + '</p>'
		elif request.args.get('divide'):
			res = a / b
			doc += '<p>' + str(a) + ' / ' + str(b) + ' = ' +  str(res) + '</p>'
	else:
		doc += '<h1>Error method type</h1>'
	doc += '</body>'
	doc += '</html>'
	return doc

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)