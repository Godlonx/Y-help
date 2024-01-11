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

def queryProject(req):
    folders = ['id','leader Id','name','summary','description']
    clearData = {}
    datas = query(req)

    for index, data in enumerate(datas):
        clearData[folders[index]] = data

    return clearData