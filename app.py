from flask import Flask, render_template, request

app = Flask(__name__)

# Home page with input form
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", result=None)

# Route to handle prediction
@app.route("/prediction", methods=["POST"])
def prediction():
    try:
        rate = float(request.form.get("rate"))
        result = round(-50.6 * rate + 90.2, 2)  # round for display
        return render_template("prediction.html", r=result)
    except Exception as e:
        return render_template("prediction.html", r=f"Error: {str(e)}")
