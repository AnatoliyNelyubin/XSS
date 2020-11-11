from flask import Flask, render_template, redirect, request

app = Flask(__name__)

current_message = ""

escaped = ""

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

@app.route('/', methods=["GET", "POST"])
def save_message():
    global current_message
    if request.method == "GET":
        return render_template("send_message.html")
    else:
        current_message = request.form.get("message")
        return redirect('xss')


@app.route('/xss')
def view_message():
    escaped = "".join([html_escape_table.get(x,x) for x in current_message])
    return render_template("view_message.html", message=current_message, protected_message=escaped)


if __name__ == '__main__':
    app.run()
