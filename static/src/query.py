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
    clearData = formatFiles(datas, folders)

    clearData['highlight'] = "/static/images/test.jpg"
    clearData['userpicture'] = "/static/images/user.png"
    clearData["level"] = 'B' if int(clearData['level']) > 5 else 'Master '+str(clearData['level'])+" "+clearData["class"]
    clearData["tags"] = tags
    return clearData



def queryHomeProject():
    datas = query("SELECT idProject, name, summary FROM Project")
    clearData = []
    for data in datas:
        clearData.append(formatFiles(data, [0,'name','summary']))

    return clearData


def formatFiles(datas, keys):
    clearData = {}
    for index, data in enumerate(datas):
        clearData[keys[index]] = data
    return clearData



def queryHomeFreelancers():
    datas = query("SELECT id, pseudo, level, class FROM User")
    print("\n\n\n=====BRUTE=====", datas, "\n\n\n")
    return datas



def queryFreelancer(id):
    datas = query("SELECT u.pseudo, u.level, u.class, f.price, f.skill, f.description FROM User as u JOIN Freelancer as f ON f.idUser = u.id WHERE u.id="+id)
    print("\n\n\n=====BRUTE=====", datas, "\n\n\n")
    return datas
