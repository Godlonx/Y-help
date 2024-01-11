from flask import Flask, render_template
import sqlite3

def query(query):
    con = sqlite3.connect("DB.db")
    cur = con.cursor()

    cur.execute(query)
    data = cur.fetchall()

    con.close()

    return data if data else ["ERROR"]
