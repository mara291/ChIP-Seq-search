from flask import Flask, render_template, request
import os
from utils import compare_data

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'bed'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    top_n = 3
    if request.method == "POST":
        if 'bedfile' not in request.files:
            return "No file uploaded", 400
        file = request.files['bedfile']
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            top_n = int(request.form.get('topn', 3))
            results = compare_data(filepath, top_n=top_n)
    return render_template("index.html", results=results, topn = top_n)
