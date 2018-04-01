# cong:utf-8
from flask import render_template,request,redirect,url_for
from app import app,db
import contextlib
from .models import UserList


@app.route("/")
@app.route("/index")
def index():
    print "------",request
    return render_template("index.html")


@app.route("/login",methods=['GET','POST'])
def login():
    print "------",request
    if request.method=='POST':
        return render_template("menu.html")
    else:
        return render_template("login.html")

@app.route("/signup",methods=['GET','POST'])
def signup():
    print "------",request
    if request.method=='POST':
        username=request.form['uname-s']
        password1=request.form['passwd-s1']
        password2=request.form['passwd-s2']
        if password1==password2:
            newuser=UserList(username=username,password=password1)
            db.session.add(newuser)
            db.session.commit()
        return redirect(url_for("login"))
    elif request.method=='GET':
        return render_template("signup.html") 

@app.route("/menu",methods=['GET','POST'])
def meun():
    print "------",request
    if request.method=='GET':
        return render_template("index.html")

@app.route("/menu/mainland")
def mainland():
    print "------",request
    return render_template("newslist.html")

@app.route("/menu/newscontent")
def newcontent():
    print "------",request
    return render_template("newscontent.html")
