# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__,template_folder="templates")
todos =[{"task":"sample todo","done":False}]

@app.route('/')
def index():
    return render_template("index.html",todos=todos)

@app.route("/add",methods =["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo,"done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>",methods =["GET","POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo["task"]= request.form["todo"]
        return redirect (url_for("index"))
    else:
        return render_template("edit_html",todo=todo,index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos [index]["done"]
    return redirect(url_for("index"))
@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__== '__main__':
    app.run(debug=True)