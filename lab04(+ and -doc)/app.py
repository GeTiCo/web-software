from flask import Flask, request

app = Flask('lab04')

@app.route('/checkbox', methods=['GET', 'POST'])
def checkbox():

    content = ''

    if (request.method == "GET"):
        color_red = request.args.get('checkbox_get_red')
        color_green = request.args.get('checkbox_get_green')
        color_blue = request.args.get('checkbox_get_blue')
    if (request.method == "POST"):
        color_red = request.form.get('checkbox_post_red')
        color_green = request.form.get('checkbox_post_green')
        color_blue = request.form.get('checkbox_post_blue')

    if (color_red != None):
        content += '<p style="color:red;">RED  NOT selected</p>'
    else:
        content += '<p style="color:black;">RED selected</p>'

    if (color_green != None):
        content += '<p style="color:green;">GREEN NOT selected</p>'
    else:
        content += '<p style="color:black;">GREEN selected</p>'

    if (color_blue != None):
        content += '<p style="color:blue;">BLUE NOT selected</p>'
    else:
        content += '<p style="color:black;">BLUE selected</p>'
    
    return result_page('Checkbox', content)

@app.route('/radiobutton', methods=['GET', 'POST'])
def radiobutton():

    content = ''

    if (request.method == "GET"):
        radio_first = request.args.get('radio_get_first')
        radio_second = request.args.get('radio_get_second')
    if (request.method == "POST"):
        radio_first = request.form.get('radio_post_first')
        radio_second = request.form.get('radio_post_second')

    if (radio_first != None):
        if (radio_first == 'RED'):
            content += '<p style="color:red;">First color RED selected</p>'
        if (radio_first == 'GREEN'):
            content += '<p style="color:green;">First color GREEN selected</p>'
        if (radio_first == 'BLUE'):
            content += '<p style="color:blue;">First color BLUE selected</p>'
    else:
        content += 'First color is not selected <br>'
    
    if (radio_second != None):
        if (radio_second == 'RED'):
            content += '<p style="color:red;">Second color RED selected</p>'
        if (radio_second == 'GREEN'):
            content += '<p style="color:green;">Second color GREEN selected</p>'
        if (radio_second == 'BLUE'):
            content += '<p style="color:blue;">Second color BLUE selected</p>'
    else:
        content += 'Second color is not selected <br>'

    return result_page('Radiobutton', content)

@app.route('/list', methods=['GET', 'POST'])
def list():

    content = ''

    if (request.method == "GET"):
        list_first = request.args.get('list1_get')
        list_second = request.args.get('list2_get')
    if (request.method == "POST"):
        list_first = request.form.get('list1_post')
        list_second = request.form.get('list2_post')

    if (list_first != '-'):
        if (list_first == 'RED'):
            content += '<p style="color:red;">First color RED selected</p>'
        if (list_first == 'GREEN'):
            content += '<p style="color:green;">First color GREEN selected</p>'
        if (list_first == 'BLUE'):
            content += '<p style="color:blue;">First color BLUE selected</p>'
    else:
        content += 'First color is not selected <br>'
    
    if (list_second != '-'):
        if (list_second == 'RED'):
            content += '<p style="color:red;">Second color RED selected</p>'
        if (list_second == 'GREEN'):
            content += '<p style="color:green;">Second color GREEN selected</p>'
        if (list_second == 'BLUE'):
            content += '<p style="color:blue;">Second color BLUE selected</p>'
    else:
        content += 'Second color is not selected <br>'

    return result_page('List', content)

def result_page(type, content):

    doc = ''

    doc += '<!doctype html>'
    doc += '<html lang="en">'
    doc += '<head>'
    doc += '<meta charset="utf-8">'
    doc += '<title>g12_Fedorenko_lab04</title>'
    doc += '</head>'
    doc += '<body>'
    doc += '<h1>' + type + '</h1>'
    doc += '<hr>'
    doc += content
    doc += '</body>'
    doc += '</html>'

    return doc

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)