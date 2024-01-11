from flask import Flask, render_template
from static.src.query import *

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return projects()

@app.route("/projects")
def projects():
    data = queryHomeProject()
    print(data)
    return render_template('home_projects.html', data=data)

@app.route("/project/<id>")
def projet(id):
    data = queryProject(id)
    print(data.keys())
    return render_template('project.html', data=data)

@app.route("/freelancers")
def freelancers():
    return render_template('home_freelancers.html')

@app.route("/freelancer/<id>")
def freelancer(id):
    return render_template('freelancer.html')

@app.route("/new")
def new():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)
