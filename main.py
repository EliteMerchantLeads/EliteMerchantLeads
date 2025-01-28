from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    industry = request.form.get("industry")
    revenue = request.form.get("revenue")

    # Save the lead to a text file (temporary storage)
    with open("leads.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Industry: {industry}, Revenue: {revenue}\n")

    return "Lead Submitted Successfully! ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
