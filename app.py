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
    data = {'id':id,'user':{'picture':'../static/images/user.png', 'name': 'Albator GRENIER', 'level':'Master 2 Informatique','mail':'Galbator@gmail.com','phone': '0805321520'} ,  'title':'Minecraft', 'highlight':'../static/images/test.jpg', 'summary':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.', 'tags':['test'], 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'}
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
