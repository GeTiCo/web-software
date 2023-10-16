from flask import Flask, request, render_template, send_file
from datetime import datetime

app = Flask('lab05')

task_list = []
color_list = []

@app.route('/')
def index():
    return send_file("static/index.html")

@app.route('/clock')
def theclock():
    time = datetime.now()
    return render_template("clock.html", cur_time=time)

@app.route('/list')
def thelist():
    global task_list
    if ("new_task" in request.args):
        new_task_name = request.args.get("new_task")
        new_task_color = request.args.get("chose_color")

        task_list.append(new_task_name)
        color_list.append(new_task_color)
    if ("delete" in request.args):
        delete_element = request.args.get("delete")
        try:
            find_index = int(delete_element) - 1
            task_list.pop(find_index)
            color_list.pop(find_index)
        except:
            pass

    return render_template("list.html", chose_color = color_list, len = len(task_list), elements=task_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)