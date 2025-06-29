from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_command():
    vendor = request.form["vendor"]
    cmd_type = request.form["cmd_type"]
    command = request.form["command"]

    output = f"Executing {cmd_type} command on {vendor.upper()} device:<br><br>{command}"
    return output

if __name__ == "__main__":
    app.run(debug=True)