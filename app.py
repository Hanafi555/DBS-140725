from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    try:
        rate = float(request.form.get("rate"))
        result = -50.6 * rate + 90.2
        return render_template("prediction.html", r=result)
    except Exception as e:
        return f"Error: {e}"

# REMOVE this line below when deploying to PythonAnywhere:
# app.run()
