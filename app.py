from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    rate = float(request.form.get("rate"))
    result = (-50.6 * rate + 90.2)
    return render_template("prediction.html", r=result)

if __name__ == "__main__":
    app.run()
