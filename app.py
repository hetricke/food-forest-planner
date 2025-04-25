from flask import Flask, request, render_template
from planner_functions import inputHandler

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        garden_length = request.form.get('length_field')
        garden_width = request.form.get('width_field')
        try:
            inputHandler.cleanInput(garden_width, garden_length)
        except:
            
            return f"ERROR"

    return render_template('index.html')

if __name__=='__main__':
    app.run()