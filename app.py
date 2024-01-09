from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home_projects.html')

@app.route("/projects")
def projects():
    return render_template('home_projects.html')

@app.route("/project/<id>")
def projet(id):
    return render_template('project.html')

@app.route("/freelancers")
def freelancers():
    return render_template('home_freelancers.html')

@app.route("/freelancer/<id>")
def freelancer(id):
    return render_template('freelancer.html')

if __name__ == '__main__':
    app.run(debug=True)