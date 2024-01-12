from flask import Flask, render_template, request
from static.src.query import *

app = Flask(__name__, template_folder='templates')

LOCALID = 2

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
    print(data['tags'])
    return render_template('project.html', data=data)

@app.route("/freelancers")
def freelancers():
    data = queryHomeFreelancer()
    return render_template('home_freelancers.html', data=data)

@app.route("/freelancer/<id>")
def freelancer(id):
    return render_template('freelancer.html')

@app.route("/new", methods=('GET', 'POST'))
def new():
    if request.method == "POST":
        price = request.form['price']
        skill = request.form['skill']
        description = request.form['description']
        insertFreelancer((LOCALID, skill, description, price))
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)
