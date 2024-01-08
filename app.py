from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/projet")
def projects():
    return render_template('projects.html')

@app.route("/projet/<id>")
def projet(id):
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)