from flask import Flask, request, render_template
from llm_wrappers import query_together 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = query_together(prompt)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
