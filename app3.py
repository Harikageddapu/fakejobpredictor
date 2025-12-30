from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("mlp_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    job_desc = request.form.get("job_desc")

    if not job_desc:
        return render_template("index.html", prediction="Please enter a job description")

    prediction = model.predict([job_desc])

    if prediction[0] == 1:
        result = "Fake Job Posting"
    else:
        result = "Real Job Posting"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)