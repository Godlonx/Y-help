from flask import Flask, render_template
import sqlite3
import numpy as np

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
    datas = query("SELECT idProject, name, summary FROM Project")[0]
    return datas



def queryHomeFreelancers():
    datas = query("SELECT id, pseudo, level, class FROM User")
    print("\n\n\n=====BRUTE=====", datas, "\n\n\n")

    #datas[2] = 'B'+datas[2]+" "+datas[3] if int(datas[2]) < 4 else 'Master '+datas[2]+" "+datas[3]

    return datas



def queryFreelancer(id):
    userData = query("SELECT pseudo, level, class FROM User WHERE id="+id)
    freelancerData = query("SELECT price, skill, description FROM Freelancer WHERE idUser="+id)
    datas = userData + freelancerData
    np.concatenate((userData, freelancerData))
    print("\n\n\n=====BRUTE=====", datas, "\n\n\n")

    return datas
