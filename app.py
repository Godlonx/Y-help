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
    data = {'id':id,'user':{'picture':'../static/img/user.png', 'name': 'Albator GRENIER', 'supInfo':['level','mail', 'Number']} ,  'title':'Minecraft', 'highlight':'../static/img/test.jpg', 'summary':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.', 'tags':['test'], 'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'}
    return render_template('project.html', data=data)

@app.route("/freelancers")
def freelancers():
    return render_template('home_freelancers.html')

@app.route("/freelancer/<id>")
def freelancer(id):
    return render_template('freelancer.html')

if __name__ == '__main__':
    app.run(debug=True)