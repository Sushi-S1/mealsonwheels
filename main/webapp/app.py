from flask import Flask, render_template

app = Flask(__name__, template_folder='C:/Users/Sushi/Documents/Github/mealsonwheels/main/Webapp')

@app.route("/")
def home():
    return render_template("index.html")

    
if __name__ == "__main__":
    app.run(debug=True)