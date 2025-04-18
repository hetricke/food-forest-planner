from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        garden_length = request.form.get('length_field')
        garden_width = request.form.get('width_field')
        return f"Length: {garden_length}\nWidth: {garden_width}"

    return render_template('index.html')

if __name__=='__main__':
    app.run()