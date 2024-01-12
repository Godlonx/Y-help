from flask import Flask, render_template
import sqlite3

def query(req):
    con = sqlite3.connect("DB.db")
    cur = con.cursor()

    cur.execute(req)
    data = cur.fetchall()
    print(data)
    con.close()

    return data

def queryProject(id):
    folders = ['name','summary','description','pseudo','level','class','email','phone']
    clearData = {}
    datas = query(f"SELECT p.name, p.summary, p.description, u.pseudo, u.level, u.class, u.email, u.phone FROM Project as p JOIN User as u ON u.id = p.idLeader WHERE p.idProject = {id}")[0]
    tags = query(f"SELECT tag.name FROM Tag JOIN TagRelation ON tag.id = TagRelation.idTag WHERE TagRelation.idProject = {id}")
    tags = ['#'+tag[0] for tag in tags]
    for index, data in enumerate(datas):
        clearData[folders[index]] = data

    clearData['highlight'] = "/static/images/test.jpg"
    clearData['userpicture'] = "/static/images/user.png"
    clearData["level"] = 'B' if int(clearData['level']) > 5 else 'Master '+str(clearData['level'])+" "+clearData["class"]
    clearData["tags"] = tags
    return clearData



def queryHomeProject():
    folders = [0,'name','summary']
    clearData = {}
    datas = query("SELECT idProject, name, summary FROM Project")[0]

    for index, data in enumerate(datas):
        clearData[folders[index]] = data

    return clearData


def queryHomeFreelancers():
    folders = [0,'pseudo','level','class']
    clearData = {}
    datas = query("SELECT id, pseudo, level, class FROM User")

    print("\n\n\n=====BRUTE=====", datas, "\n\n\n")

    #tags = ['#'+str(item) for item in data[0]]
    for index, data in enumerate(datas):
        clearData[folders[index]] = data

    clearData["level"] = 'B'+clearData['level']+" "+clearData["class"] if int(clearData['level']) < 4 else 'Master '+clearData['level']+" "+clearData["class"]

    return clearData
