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
    clearData["level"] = 'B'+str(clearData['level'])+" "+clearData["class"] if int(clearData['level']) < 4 else 'Master '+str(clearData['level']-3)+" "+clearData["class"]
    clearData["tags"] = tags
    return clearData



def queryHomeProject():
    datas = query("SELECT idProject, name, summary FROM Project")
    clearData = []
    for data in datas:
        clearData.append(formatFiles(data, [0,'name','summary']))

    return clearData

def queryHomeFreelancer():
    pass

def formatFiles(datas, keys):
    clearData = {}
    for index, data in enumerate(datas):
        clearData[keys[index]] = data
    return clearData



def insertProject(data):
    con = sqlite3.connect('DB.db')
    cursor = con.cursor()
    data = (data[0], data[1], data[2], data[3], data[4], data[5])
    cursor.execute(f"INSERT INTO Project (idProject, idLeader, name, summary, description, picture) VALUES (?, ?, ?, ?, ?, ?)", data)
    con.commit()
    print("inserted")
    cursor.close()
    con.close()

def insertFreelancer(data):
    con = sqlite3.connect('DB.db')
    cursor = con.cursor()
    data = (data[0], data[1], data[2], int(data[3]))
    cursor.execute(f"INSERT INTO Freelancer (idUser, skill, description, price) VALUES (?, ?, ?, ?)", data)
    con.commit()
    print("inserted")
    cursor.close()
    con.close()



def queryHomeFreelancers():
    datas = query("SELECT id, pseudo, level, class FROM User")

    clearData = []
    for data in datas:
        bruteData = formatFiles(data, [0,'pseudo','level','class'])
        bruteData["level"] = 'B'+str(bruteData['level'])+" "+bruteData["class"] if int(bruteData['level']) < 4 else 'M'+str(bruteData['level']-3)+" "+bruteData["class"]
        clearData.append(bruteData)
    return clearData



def queryFreelancer(id):
    datas = query("SELECT u.pseudo, u.level, u.class, f.price, f.skill, f.description FROM User as u JOIN Freelancer as f ON f.idUser = u.id WHERE u.id="+id)[0]

    clearData = formatFiles(datas, ['pseudo','level','class','price','skill','description'])
    print("\n\n\n\n\n\n", clearData, "\n\n\n\n\n\n")
    clearData["level"] = 'B'+str(clearData['level'])+" "+clearData["class"] if int(clearData['level']) < 4 else 'M'+str(clearData['level']-3)+" "+clearData["class"]

    return clearData
