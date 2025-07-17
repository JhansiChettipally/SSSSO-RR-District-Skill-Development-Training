from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    heads = tails = 0
    flips = 0
    results = []

    if request.method == "POST":
        try:
            flips = int(request.form["flips"])
            if flips <= 0:
                return render_template("index.html", error="Please enter a positive number.")

            for _ in range(flips):
                toss = random.choice(["Heads", "Tails"])
                results.append(toss)
                if toss == "Heads":
                    heads += 1
                else:
                    tails += 1

            return render_template("index.html", flips=flips, results=results, heads=heads, tails=tails)

        except ValueError:
            return render_template("index.html", error="Invalid input. Please enter a number.")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
