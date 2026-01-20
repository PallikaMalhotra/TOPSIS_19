from flask import Flask, render_template, request, send_file
import os
from topsis_logic import run_topsis

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    file = request.files["file"]
    weights = request.form["weights"]
    impacts = request.form["impacts"]

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    output_path = run_topsis(
        input_path,
        weights,
        impacts,
        OUTPUT_FOLDER
    )

    # 🔽 DOWNLOAD HAPPENS HERE
    return send_file(
        output_path,
        as_attachment=True,
        download_name="topsis_result.csv"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

