from flask import Flask, render_template
import sqlite3

def query(req):
    con = sqlite3.connect("DB.db")
    cur = con.cursor()
    
    cur.execute(req)
    data = cur.fetchall()
    con.close()

    cleaned_data = [str(item) for item in data[0]]
    return cleaned_data



def queryProject(id):
    folders = ['name','summary','description','pseudo','level','class','email','phone']
    clearData = {}
    datas = query(f"SELECT p.name, p.summary, p.description, u.pseudo, u.level, u.class, u.email, u.phone FROM Project as p JOIN User as u ON u.id = p.idLeader WHERE p.idProject = {id}")
    tags = query(f"SELECT tag.name FROM Tag JOIN TagRelation ON tag.id = TagRelation.idTag WHERE TagRelation.idProject = {id}")
    for index, data in enumerate(datas):
        clearData[folders[index]] = data

    clearData['highlight'] = "/static/images/test.jpg"
    clearData['userpicture'] = "/static/images/user.png"
    clearData["level"] = 'B' if int(clearData['level']) > 5 else 'Master '+clearData['level']+" "+clearData["class"]
    clearData["tags"] = tags
    return clearData



def queryHomeProject():
    folders = [0,'name','summary']
    clearData = {}
    datas = query("SELECT idProject, name, summary FROM Project")

    for index, data in enumerate(datas):
        clearData[folders[index]] = data

    return clearData


def queryHomeFreelancer():
    folders = [0,'name','summary']
    clearData = {}
    datas = query("SELECT idProject, name, summary FROM Project")

    for index, data in enumerate(datas):
        clearData[folders[index]] = data

    return clearData
