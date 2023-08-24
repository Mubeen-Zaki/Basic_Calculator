from flask import Flask,request,render_template,jsonify
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/math", methods = ['POST'])
def calculate():
    if request.method == "POST":
        op = request.form["operation"]
        a = request.form["num1"]
        b = request.form["num2"]
        if op == "add":
            r = int(a) + int(b)
        elif op == "subtract":
            r = int(a) - int(b)
        elif op == "multiply":
            r = int(a) * int(b)
        elif op == "divide":
            r = int(a) / int(b)
        else:
            r = math.log(int(a),int(b))
        res = f"Result for {op} op for {a}, {b} is {str(r)}"
        return render_template('results.html',result = res)

@app.route("/postman_action", methods = ['POST'])
def calculate1():
    if request.method == "POST":
        op = request.json["operation"]
        a = request.json["num1"]
        b = request.json["num2"]
        if op == "add":
            r = int(a) + int(b)
        elif op == "subtract":
            r = int(a) - int(b)
        elif op == "multiply":
            r = int(a) * int(b)
        elif op == "divide":
            r = int(a) / int(b)
        else:
            r = math.log(int(a),int(b))
        res = f"Result for {op} op for {a}, {b} is {str(r)}"
        return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0")