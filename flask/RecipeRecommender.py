from flask import Flask, redirect, url_for, render_template, request, session

import random, os, subprocess

app = Flask(__name__)
app.secret_key = "cookbook"

@app.route("/")
def home():
    return render_template("Welcome.html")

@app.route("/EnterName", methods=["POST", "GET"])
def Name():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("EnterName.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("RecipeRecommender.html", usr = user)
    else:
        return redirect(url_for("/login"))


@app.route("/RecipeRecommender")
def RecipeFinder():
    return render_template("RecipeRecommender.html")

# Random recipe selecter


@app.route("/RandomRecipe")
def RandomRecipe():
    path = r"C:\Users\Jovani\Desktop\Project\Recipes"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path,x))
    ])
    Directory = os.path.realpath(random_filename)
    return render_template("RandomRecipe.html", randRecipe = random_filename, dir= Directory)



@app.route("/ShoppingList")
def ShoppingList():
    return render_template("ShoppingList.html")
## using an f string to import custom names
# @ app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

#practice using rerouting
# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin"))



if __name__ == "__main__":
    app.run(debug=True)
