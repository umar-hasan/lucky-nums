from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route('/api/get-lucky-num', methods=["POST"])
def lucky_num_data():
    error = {"error": {}}
    color_list = ["red", "blue", "green", "orange"]
    
    if not request.json:
        return {"error": {
            "name": "Name is required.",
            "email": "Email is required.",
            "year": "Year is required.",
            "color": "Color is required."
        }}
    if "name" not in request.json or request.json["name"] is "":
        error["error"]["name"] = "Name is required."
    if "email" not in request.json or request.json["email"] is "":
        error["error"]["email"] = "Email is required."
    if "year" not in request.json or request.json["year"] is "":
        error["error"]["year"] = "Year is required."
    elif int(request.json["year"]) < 1900 or int(request.json["year"])> 2000:
        error["error"]["year"] = "Year must be between 1900 and 2000, inclusive."
    if "color" not in request.json or request.json["color"] is "":
        error["error"]["color"] = "Color is required."
    elif request.json["color"].lower() not in color_list:
        error["error"]["color"] = "Invalid color."

    if len(error["error"]) != 0:
        return jsonify(error)
    
    year = request.json["year"]
    rand_num = random.randint(1, 100)

    res_num = requests.get(f"http://numbersapi.com/{rand_num}/year")
    res_year = requests.get(f"http://numbersapi.com/{year}/year")
    

    return {
        "num": {
            "fact": f"{res_num.text}",
            "num": rand_num
        },
        "year": {
            "fact": f"{res_year.text}",
            "year": year
        }}