from flask import Flask ,render_template,request,session
app = Flask(__name__)
app.secret_key="mysecretkey"

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"]=[]
    result = None
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        c = request.form["c"]
        if c=="+":
            result = f"{a} + {b} = {a + b}"
        elif c=="-":
            result = f"{a} - {b} = {a - b}"
        elif c=="*":
            result = f"{a} * {b} = {a * b}"
        elif c=="/":
            result = f"{a} / {b} = {a / b}"

        session["history"]=session["history"]+[result]
    return render_template("index.html", result=result,history=session["history"])
if __name__ == "__main__":
    app.run(debug=True)